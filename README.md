/ Custom user models

http POST http://127.0.0.1:8000/api/users/create/ username="carmeella" password="helloworld1"

http POST http://127.0.0.1:8000/api/users/create/ email="carmeella@example.com" password="helloworld1"
> Success

/ JWT login

http POST http://127.0.0.1:8000/api/jwt/create/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/api/me/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4NzA2MSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.0GzSV7Ih_JsNwh4a1i1obzlsajtftszI12238WoY9Gw'
> Returns info

/ Custom paths

http POST http://127.0.0.1:8000/api/user/login/ email="carmeella@example.com" password="helloworld1"
> Returns token

http GET http://127.0.0.1:8000/user/view/ 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImNhcm1lZWxsYUBleGFtcGxlLmNvbSIsImV4cCI6MTU2MDQ4NzA2MSwiZW1haWwiOiJjYXJtZWVsbGFAZXhhbXBsZS5jb20ifQ.0GzSV7Ih_JsNwh4a1i1obzlsajtftszI12238WoY9Gw'
> Returns info