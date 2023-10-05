import sys

def main(tipe):
    n = 9
    alphabet = [chr(i) for i in range(65, 91)]
    
    for i in range(n):
        for j in range(n):
            if((i == n-1) or (i == 0)):
                if(tipe==1):
                    print("*",end=" ")
                elif(tipe==2):
                    print(j+1,end=" ")
                elif(tipe==3):
                    print(alphabet[j],end=" ")
            elif((j == i) or (j == n-i-1)):
                if(tipe==1):
                    print("*",end=" ")
                elif(tipe==2):
                    if(i<n/2):
                        print(j+1-i,end=" ")
                    else:
                        print(j+1-i+(2*(i-int(n/2))),end=" ")
                elif(tipe==3):
                    if(i<n/2):
                        print(alphabet[j-i],end=" ")
                    else:
                        print(alphabet[j-i+(2*(i-int(n/2)))],end=" ")
            else:
                print(" ",end=" ")
        print("")

if __name__ == "__main__":
    if len(sys.argv) != 2 or int(sys.argv[1]) not in [1, 2, 3]:
        print("Cara run program: python (filename).py <tipe pola>")
    else:
        tipe = int(sys.argv[1])
        main(tipe)