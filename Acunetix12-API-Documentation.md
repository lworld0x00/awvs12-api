## 创建组

### api

{api_base_url}/api/v1/target_groups

### method

POST

### request payload

{"name":"test","description":""}





target_id: 

708de1ea-26cb-42ce-9dc6-28eae2ab5fda



group_id:

28a2d96882c04124a62a8431142521ff



28a2d968-82c0-4124-a62a-8431142521ff



{'Location': '/api/v1/target_groups/4cb2d9045c2c4e5b8fe5d6046d091d6d', 'Content-type': 'application/json; charset=utf8', 'Pragma': 'no-cache', 'Expires': '-1', 'Cache-Control': 'no-cache, must-revalidate', 'Date': 'Wed, 09 Oct 2019 16:00:56 GMT', 'Transfer-Encoding': 'chunked'}

## 将target加入组中

### api

{api_base_url}/api/v1/target_groups/3dc94f87-308e-40d9-9a5a-bd85ca9e68b3/targets



3dc94f87-308e-40d9-9a5a-bd85ca9e68b3: 猜测是group id

### method

PATCH

### request payload

{"add":["4d30f3f3-c44e-48d9-b126-fcac1c79b812"],"remove":[]}



4d30f3f3-c44e-48d9-b126-fcac1c79b812： 猜测是target id 需要进一步测试