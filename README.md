### Patent server     ![](https://travis-ci.org/danhammer/patent-server.svg?branch=master)

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

[http://patent-server.appspot.com/api?query=7654321](http://patent-server.appspot.com/api?query=7654321)

```json
{
    "type": "patent number",
    "number": "7654321",
    "title": "Formation fluid sampling apparatus and methods"
}
```
