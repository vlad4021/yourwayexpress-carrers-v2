from sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://p1f9ilqppjlsq9fan5uf:pscale_pw_O0WiCKHE8mtH1z4ito6M41T3Vd3TiacAZuyp2KczoN9@aws.connect.psdb.cloud/yourwayexpresscarrers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca" : "/etc/ssl/cert.pem"
    }
  })


