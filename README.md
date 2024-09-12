## First Endpoint:
GET /hello?name={SOME_NAME}

Response should be as application/json like this:
{
  "greeting": "Hello, {SOME_NAME}"
}
If no name is provided, then the response should be:
{ 
   "greeting": "Hello, World!"
}
![Screenshot 2024-09-02 173020](https://github.com/user-attachments/assets/08436f16-6260-4e46-870b-153b7f593c38)

![Screenshot 2024-09-02 173117](https://github.com/user-attachments/assets/117f8fc3-7f81-463c-9b25-3411518a14c2)


## Second Endpoint:
GET /info

Response should as application/json. It should contain the following information:
- Request time formatted in ISO8601
- Client IP Address
- Server/Host name
- Client Request Headers

Example response:
{
  "time": "2024-08-24T14:15:12Z",
  "client_address": "192.168.1.1",
  "host_name": "my-great-server",
  "headers": {
    "Accept": "all",
    "User-Agent": "curl 1/123"
  }
}
![image](https://github.com/user-attachments/assets/74f2a9d9-d1cf-4319-a888-8ae6149285af)

Note: proper response headers should be set like Content-Type
