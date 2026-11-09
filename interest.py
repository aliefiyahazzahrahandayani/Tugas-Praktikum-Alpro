def compound_interest(principal, rate, time):
    # Masukkan rumus bunga majemuk: future value =  principal * (1 + rate)^time
    return principal * ((1 + rate) ** time)
def simple_interest(principal, rate, time):
    # Rumus Bunga Sederhana: Awal + (Awal * bunga * waktu)
    return principal + (principal * rate * time)