def fizzbuzz(n):
    for i in range(1, n+1):
        result = ""

        if i%3 == 0:
            result+="fizz"
        if i%5==0:
            result+="buzz"
        if result == "":
            result = i
        if i%15==0:
            result+=""

        print(result)

fizzbuzz(30)
