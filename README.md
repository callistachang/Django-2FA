# CLI Test Cases

## Custom user models

http POST http://127.0.0.1:8000/api/users/create/ username="carmeella" password="helloworld1"

http POST http://127.0.0.1:8000/api/users/create/ email="carmeella@example.com" password="helloworld1"
> Success

## JWT login

http POST http://127.0.0.1:8000/api/jwt/create/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/me/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4NzA2MSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.0GzSV7Ih_JsNwh4a1i1obzlsajtftszI12238WoY9Gw'
> Returns info

## Custom paths

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4NzA2MSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.0GzSV7Ih_JsNwh4a1i1obzlsajtftszI12238WoY9Gw'
> Returns info

## JWT logout

http POST http://127.0.0.1:8000/api/user/create/ email="carmeella@example.com" password="helloworld1"
> Success

http POST http://127.0.0.1:8000/api/user/create/ email="rezinomrah@example.com" password="helloworld1"
> Success

sqlite3 db.sqlite3 "SELECT jwt_secret FROM SpaApp_spauser"
> Different jwt_secret generated per user:
> b5283b08539645bdbe07abc08fbfa5f1
> 6de2cfcc1aef4684a179500f569ce21a

## TOTP

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/totp/create/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4ODYwMSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.Ci2IcSMMivmAgjaLdU9XaxFDCECEgFWAKqVR25Xmies"
> "otpauth://totp/carmeella%40example.com?secret=BVU3JHC6POLKNTOGMWZZIJDIADF4655H&algorithm=SHA1&digits=6&period=30"
> Enter the secret key into Google Authenticator

http POST http://127.0.0.1:8000/api/totp/login/938181/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4ODYwMSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.Ci2IcSMMivmAgjaLdU9XaxFDCECEgFWAKqVR25Xmies"
> true

## Custom JWT payload

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4OTMwOSwib3RwX2RldmljZV9pZCI6bnVsbH0.tRQkdMYD4biFwzhZOZ-J1dlu2Jm99kbrNjKdTl2j9v4'
> Returns info

![jwt.io](jwtio.png)

## Storing an OTP identifier in the JWT

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http POST http://127.0.0.1:8000/api/totp/login/084060/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MDE1MCwib3RwX2RldmljZV9pZCI6bnVsbH0.RzkUkGPIiyFoekM0vtuJtcRbyYRbiv4Dbdq7vvdFpw0"
> Returns new JWT token with OTP verification information

![jwt.io](jwtio2.png)

## Custom permissions

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MjIxNSwib3RwX2RldmljZV9pZCI6Im90cF9zdGF0aWMuc3RhdGljZGV2aWNlLzEifQ.rtcoL-A16Q18j55rk9ROjnKXAWbIW8i9mGrUmKx8w_w'
> "detail": "You do not have permission to perform this action until you verify your OTP device."

http POST http://127.0.0.1:8000/api/totp/login/369276/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MDY2Miwib3RwX2RldmljZV9pZCI6bnVsbH0.OLHy_sEzDJDg2MZhidvOFz67R9hskXn90Gj74OGxwiw'
> Returns new JWT token with OTP verification information (TOTP device)
> Try again with the new JWT token

http GET http://127.0.0.1:8000/api/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MDc3OCwib3RwX2RldmljZV9pZCI6Im90cF90b3RwLnRvdHBkZXZpY2UvMSJ9.nk4DJpAhjM7sqI2Vwq7uNLxqSQT6z6jjA7aLgxPANaE'
> Returns info successfully

## Emergency codes if you lose your TOTP device

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http POST http://127.0.0.1:8000/api/totp/login/713261/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MTM3OCwib3RwX2RldmljZV9pZCI6bnVsbH0.Og8HeFWAjI6v9B1-Bp3QZauBu5rVbMxRvPRn_iGXRek'
> Returns new JWT token with OTP verification information

http GET http://127.0.0.1:8000/api/static/create/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MjAyNiwib3RwX2RldmljZV9pZCI6Im90cF90b3RwLnRvdHBkZXZpY2UvMSJ9.umBLx9xsBDcypsxwH4eyndzShGhOJn3y-Rhr2pP_53Q"
> "5dlxc4j7", "gvpnoxgu", "dvmkqpsb", "uykbc5wv", "4i2zq2ni", "4e4x4z4c"

http POST http://127.0.0.1:8000/api/static/login/5dlxc4j7/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MjA1Niwib3RwX2RldmljZV9pZCI6bnVsbH0.0XVzFChaTXmgPnL_JyD-cm8Z-gCAiH0CTD2cM3d_qrg'
> Use a payload that didn't have permission
> Returns new token with OTP verification information (static device)
> Try again with the new JWT token

![jwt.io](jwtio3.png)

http GET http://127.0.0.1:8000/api/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ5MDc3OCwib3RwX2RldmljZV9pZCI6Im90cF90b3RwLnRvdHBkZXZpY2UvMSJ9.nk4DJpAhjM7sqI2Vwq7uNLxqSQT6z6jjA7aLgxPANaE'
> Returns info successfully