# Pretty JWT

Simple utility for viewing JWT tokens in console.

## Install

```shell
pip install pretty_jwt
```

## Use

```shell
pjwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9obiBEb2UifQ.DjwRE2jZhren2Wt37t5hlVru6Myq4AhpGLiiefF69u8

Header:
{
    "alg": "HS256",
    "typ": "JWT"
}
Payload:
{
    "name": "John Doe"
}
Signature:
DjwRE2jZhren2Wt37t5hlVru6Myq4AhpGLiiefF69u8
```