from flask import Flask, request, jsonify
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib
import requests

app = Flask(__name__)

@app.route('/funsystem', methods=['GET', 'POST'])
def funsystem_func():
    req = request.get_json()

    url = "https://fun.ssu.ac.kr/ko/program/all/list/all/{}"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    funsystems = soup.find("ul", attrs={"class": "columns-4"}).find_all("li")
    answer_cal = []
    answer_link = []
    for funsystem in funsystems:
        calums = funsystem.find("b", attrs={"class": "title"})
        link = funsystem.a["href"]
        time = funsystem.find_all("small")
        for item in time:
            timetxt = item.get_text()
        answer_cal.append(calums.text)
        answer_link.append(link)

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "펀시스템",
                                "description": answer_cal[0],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[0]
                                    }
                                ]
                            },
                            {
                                "title": "펀시스템",
                                "description": answer_cal[1],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[1]
                                    }
                                ]
                            },
                            {
                                "title": "펀시스템",
                                "description": answer_cal[2],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[2]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return jsonify(res)


#NOTICE
@app.route('/notice', methods=['GET', 'POST'])
def notice_func():
    req = request.get_json()

    #location = req["action"]["detailParams"]["sys_location"]["value"]

    url = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/page/1/"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text)

    notices = soup.find_all("a", attrs = {"class": "text-decoration-none d-block text-truncate"})
    answer_cal = []
    answer_link = []
    for n in notices:
        calums = n.find("span", attrs = {"class" : "d-inline-blcok m-pt-5"})
        link = "https://scatch.ssu.ac.kr/" + n["href"]
        answer_cal.append(calums.text)
        answer_link.append(link)

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "공지사항",
                                "description": answer_cal[0],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[0]
                                    }
                                ]
                            },
                            {
                                "title": "공지사항",
                                "description": answer_cal[1],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[1]
                                    }
                                ]
                            },
                            {
                                "title": "공지사항",
                                "description": answer_cal[2],
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "보러가기",
                                        "webLinkUrl": answer_link[2]
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return jsonify(res)


# 메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)