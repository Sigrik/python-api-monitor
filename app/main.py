import json
from checker import check_url

def main():
   with open("app/config.json") as f:
       config = json.load(f)

   results = []

   for url in config["urls"]:
       result = check_url(url)
       print(result)
       results.append(result)

   with open("logs.json", "w") as f:
       json.dump(results, f, indent=2)

if __name__ == "__main__":
   main()
