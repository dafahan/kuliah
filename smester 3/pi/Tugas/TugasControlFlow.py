
def main():
    """Ibu Pergi Ke Pasar """
    state = int(input("Masukan Jumlah Ayam yang tersedia ,jika habis input 0: "))
    if(state):
        print("Ibu Memasak Ayam")
        return
    
    """Ibu Memasak dan membeli Tempe"""
    state = int(input("Masukan Jumlah potongan tempe yang dibutuhkan : "))
    counter = 0
    while state>counter:
        print("Jumlah Potongan Masih Kurang ",state-counter)
        counter+=1
    print("Jumlah Tempe Cukup")

if __name__ == "__main__":
    main()

