import pandas as pd
import numpy as np
from sqlalchemy import create_engine

np.random.seed(42)

engine = create_engine(
"postgresql+psycopg2://postgres@localhost:5432/Channel_Profitability"
)

# DATE RANGE

dates = pd.date_range("2025-01-01","2026-02-28")

# FX RATES

usd = 30
fx_data = []

for d in dates:

    monthly_shock = 1.02 if d.day <= 2 else 1.0
    trend = 0.0008

    usd *= (1 + trend + np.random.uniform(-0.002,0.003)) * monthly_shock

    eur = usd * np.random.uniform(1.07,1.12)

    fx_data.append([
        d.date(),
        round(usd,4),
        round(eur,4),
        "TL"
    ])

df_fx = pd.DataFrame(
fx_data,
columns=["rate_date","usd_to_tl","eur_to_tl","base_currency"]
)

# INTEREST RATES

rates = []

base_rate = 35

for d in dates:

    base_rate += np.random.uniform(-0.05,0.08)

    rates.append([
        d.date(),
        round(base_rate,2)
    ])

df_interest = pd.DataFrame(
rates,
columns=["rate_date","annual_rate"]
)

# PRODUCTS


products = []

pid = 1

for i in range(8):
    products.append((pid,f"Premium Product {i+1}","Premium","Apparel"))
    pid+=1

for i in range(12):
    products.append((pid,f"Mid Product {i+1}","Mid","Apparel"))
    pid+=1

for i in range(20):
    products.append((pid,f"Entry Product {i+1}","Entry","Apparel"))
    pid+=1

df_products = pd.DataFrame(
products,
columns=["product_id","product_name","segment","category"]
)

# PRODUCTION COSTS

costs = []

for _,row in df_products.iterrows():

    if row.segment=="Premium":

        raw=np.random.uniform(70,120)
        labor=np.random.uniform(1200,1800)

    elif row.segment=="Mid":

        raw=np.random.uniform(15,40)
        labor=np.random.uniform(400,900)

    else:

        raw=np.random.uniform(3,10)
        labor=np.random.uniform(150,400)

    costs.append([
        row.product_id,
        "2025-01-01",
        round(raw,2),
        round(labor,2),
        round(np.random.uniform(50,200),2)
    ])

df_costs = pd.DataFrame(
costs,
columns=[
"product_id",
"effective_cost_date",
"raw_material_usd",
"labor_tl",
"other_costs_tl"
]
)

# PAYMENT TERMS

terms = [
(1,"D2C-Cash",0,0),
(2,"B2B-30D",30,1),
(3,"B2B-60D",60,2),
(4,"B2B-90D",90,4)
]

df_terms = pd.DataFrame(
terms,
columns=[
"term_id",
"term_name",
"days_to_payment",
"discount_rate"
]
)

# PRICE STRUCTURE

segment_price = {
"Premium": np.random.uniform(350,600),
"Mid": np.random.uniform(120,250),
"Entry": np.random.uniform(25,60)
}

products_by_segment = {
seg: df_products[df_products.segment==seg].product_id.values
for seg in ["Premium","Mid","Entry"]
}

# ORDERS

orders = []

order_id = 100000

for d in dates:

    if d.month==11:
        multiplier=3
    elif d.month in [6,7]:
        multiplier=1.5
    elif d.month in [1,2]:
        multiplier=0.8
    else:
        multiplier=1

    base_orders=np.random.poisson(25)

    daily_orders=int(base_orders*multiplier)

    fx_row=df_fx[df_fx.rate_date==d.date()].iloc[0]

    usd_to_tl=fx_row.usd_to_tl
    eur_to_tl=fx_row.eur_to_tl

    usd_to_eur=eur_to_tl/usd_to_tl

    for _ in range(daily_orders):

        order_id+=1

        segment=np.random.choice(
        ["Premium","Mid","Entry"],
        p=[0.2,0.4,0.4]
        )

        product_id=np.random.choice(products_by_segment[segment])

        if segment=="Premium":
            channel=np.random.choice(["D2C","B2B"],p=[0.75,0.25])

        elif segment=="Entry":
            channel=np.random.choice(["D2C","B2B"],p=[0.4,0.6])

        else:
            channel=np.random.choice(["D2C","B2B"],p=[0.55,0.45])

        if channel=="D2C":

            qty=np.random.randint(1,4)
            term_id=1
            commission=18 if segment=="Premium" else 15
            returned=np.random.rand()<0.15

        else:

            qty=np.random.randint(20,150)
            term_id=np.random.choice([2,3,4],p=[0.5,0.35,0.15])
            commission=0
            returned=np.random.rand()<0.02

        base_usd=segment_price[segment]

        if channel=="B2B":
            base_usd*=0.65

        currency=np.random.choice(["TL","EUR"],p=[0.5,0.5])

        if currency=="TL":

            unit_price=base_usd*usd_to_tl

        else:

            unit_price=base_usd/usd_to_eur

        settlement=d+pd.Timedelta(
        days=int(
        df_terms[df_terms.term_id==term_id]
        .days_to_payment.values[0]
        )
        )

        orders.append([
        order_id,
        d.date(),
        product_id,
        channel,
        qty,
        round(unit_price,2),
        round(base_usd,2),
        currency,
        d.date(),
        term_id,
        commission,
        returned,
        settlement.date()
        ])

df_orders=pd.DataFrame(
orders,
columns=[
"order_id",
"order_date",
"product_id",
"channel",
"quantity",
"unit_price_currency",
"unit_price_usd",
"currency",
"exchange_rate_date",
"payment_term_id",
"platform_commission_rate",
"is_returned",
"settlement_date"
]
)

# MARKETING & LOGISTICS

campaigns=[
"Instagram Ads",
"Google Shopping",
"Black Friday",
"Summer Campaign"
]

marketing=[]

for d in dates:

    for seg in ["Premium","Mid","Entry"]:

        for channel in ["D2C","B2B"]:

            campaign=np.random.choice(campaigns)

            if channel=="D2C":

                spend=np.random.uniform(2000,6000)

                if d.month==11:
                    spend*=3

            else:

                spend=np.random.uniform(200,800)

            shipping=np.random.uniform(80,150) if channel=="D2C" else np.random.uniform(1500,3000)

            returns=np.random.randint(1,10) if seg!="Entry" else np.random.randint(5,20)

            marketing.append([
            d.date(),
            channel,
            seg,
            campaign,
            round(spend,2),
            round(shipping,2),
            returns,
            round(returns*np.random.uniform(40,120),2)
            ])

df_marketing=pd.DataFrame(
marketing,
columns=[
"date",
"channel",
"segment",
"campaign_name",
"marketing_spend_tl",
"shipping_cost_tl",
"return_count",
"return_cost_tl"
]
)


# WRITE TO DATABASE

df_fx.to_sql("fx_rates",engine,if_exists="append",index=False)
df_interest.to_sql("interest_rates",engine,if_exists="append",index=False)
df_products.to_sql("products",engine,if_exists="append",index=False)
df_costs.to_sql("production_costs",engine,if_exists="append",index=False)
df_terms.to_sql("payment_terms",engine,if_exists="append",index=False)
df_orders.to_sql("orders",engine,if_exists="append",index=False)
df_marketing.to_sql("marketing_and_logistics",engine,if_exists="append",index=False)

print("Dataset generated successfully")