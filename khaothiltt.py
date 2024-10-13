import httpx
from bs4 import BeautifulSoup


HTML_PARSER = "html.parser"


class khaothiltt:
    def __init__(self) -> None:
        self.client = httpx.Client(
            http2 = True,
            base_url = "https://khaothiltt.nhpoj.net",
        )
        

    def getAllClass(self):
        resp = self.client.get(url="/tkb/index.php")
        parser =  BeautifulSoup(resp.text, HTML_PARSER)
        return str(parser.select("datalist#lops > option")[0]) \
                .strip() \
                .replace("</option>", "") \
                .replace('<option value="', "") \
                .replace('">', "") \
                .strip() \
                .split("\n")
            # fuck, bs4 suck!
                        
                
    def getTKB(self, lop: str):
        resp = self.client.post(
            url = "/tkb/index.php",
            data = {"lop": lop.strip().upper()}
        )
        parser = BeautifulSoup(resp.text, HTML_PARSER)
        return [[[obj.get_text(strip=True) for obj in rows.select("td")][1:] for (i, rows) in enumerate(table.select("tr")) if i!=0] for table in parser.select("table")] # One-Liner For LeKhoi :v
        
    

if __name__ == "__main__":
    ktltt = khaothiltt()
    print(ktltt.getAllClass())
    sang, chieu = ktltt.getTKB(lop="10A2")

    # import pandas as pd
    # cols = [f"Thứ {i}" for i in range(2, 7+1)]
    # print(pd.DataFrame(sang, columns=cols))
    # print(pd.DataFrame(chieu, columns=cols))

    print(f"Thoi khoa bieu cua Thu Hai (buoi sang): {list(zip(*sang))[0]}")
    print(f"Thoi khoa bieu cua Thu Ba (buoi Chieu): {list(zip(*chieu))[1]}")