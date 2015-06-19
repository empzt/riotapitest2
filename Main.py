mykey='06cd112f-ac86-4ff0-bb5e-8771de1a7668'

from RiotAPI import RiotAPI

myname='piro167'
def main():
    api = RiotAPI(mykey)
    r = api.get_summoner_by_name(myname)
    print r['piro167']['id']


if __name__ == "__main__":
    main()
