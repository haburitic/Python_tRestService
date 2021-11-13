# Python_tRestService

#Service post, + request 
curl -X POST \
  http://localhost:5000/add_Empleado \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: e874dc6b-83cd-b430-13b6-0c36c087d02f' \
  -d '{
            "nombre":"Javier" ,
            "apellido": "zapata",
            "numeroDocumento": "6565632"

        }'
		
		
#service get
curl -X GET \
  http://localhost:5000/todo/api/task/1 \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 98a80020-9e61-ecf2-4c59-2dca6096134e'