# Patent server

Return the metadata associated with patent and patent application numbers in a RESTful sort of way.

**HTTP Request**:

```bash
GET http://patent-server.appspot.com/api
```

**Parameters**:

parameter  | type
---------- | -------------
query      | character sequence

**Example**:
[http://patent-server.appspot.com/api?query=7777777](http://patent-server.appspot.com/api?query=7777777)

```json
{
    "type": "patent number",
    "number": "7777777",
    "title": "System and method for active call monitoring"
}
```
