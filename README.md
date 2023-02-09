# Pretty JWT

Simple utility for viewing JWT tokens in console.

## Install

```shell
pip install pretty_jwt
```

## Use

```shell
pjwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMj ... Y3NjA2NTU0NX0.-dX97s4EAnyoXt6G4aHBV_dZD-IzwIvW9eOZ-DNBw1A
Header:
{
    "alg": "HS256",
    "typ": "JWT"
}
Payload:
{
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1675977465,
    "exp": 1676151945,
    "nbf": 1676065545
}
Signature:
-dX97s4EAnyoXt6G4aHBV_dZD-IzwIvW9eOZ-DNBw1A

Expiration Time : 2023-02-11 22:45:45
Issued At       : 2023-02-09 22:17:45
Not Before      : 2023-02-10 22:45:45
```
