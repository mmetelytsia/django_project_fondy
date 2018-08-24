# django_project_fondy

Django sample project

1. Fire up docker compose:

`docker-compose up -d --build`

2. Open app bash:

`docker exec -ti fondy_web_1 /bin/bash`

3. Load data to database:

   * `cd database`
   * run `python export_data_to_postgres.py`
   * or with parameters
   * `python export_data_to_postgres.py --file 9890.csv --schema_name pineapple_orders --if_exists replace`

4. Test the endpoint:

  GET http://127.0.0.1:8000/orders/66996325/
  
`[{"model": "pineapple.orders", "pk": 0, "fields": {"internal_id": 66996325, "time_of_order_creation": "20.11.17 16:11:18", "merchant_id": 1397120, "status": "processing", "sum": "4,05", "currency": "USD", "order_id": "demo35681260", "order_type": "verification", "order_description": "demo"}}]`

  GET http://127.0.0.1:8000/orders/66996326/
  
`Record with internal id 66996326 does not exist`
