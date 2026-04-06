# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    return price * (1 + tax_pct / 100)


def final_price(price, quantity, discount_pct, tax_pct):

    subtotal = price * quantity

    con_descuento = apply_discount(subtotal, discount_pct)

    con_impuesto = apply_tax(con_descuento, tax_pct)

    decimales = round(con_impuesto, 2)
    return decimales


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):

    precio_a = final_price(price_a, qty_a, disc_a, tax_pct)
    precio_b = final_price(price_b, qty_b, disc_b, tax_pct)

    if precio_a <= precio_b:
        return "A"
    else:
        return "B"