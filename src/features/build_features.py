from apyori import apriori

if __name__ == "__main__":

    transactions = [
        ['beer', 'nuts'],
        ['beer', 'cheese'],
    ]

    results = list(apriori(transactions))

    print(results)
