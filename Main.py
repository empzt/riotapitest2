mykey='****'
from RiotAPI import RiotAPI

def main():
    api=RiotAPI(mykey)
    r = api.get_summoner_by_name('Piro167')
    print r

if __name__ == "__main__":
    main()
