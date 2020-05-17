import meraki

apikey = '<Introduce tu llave de API aqui>'
baseurl = 'https://api.Meraki.com/api/v0'

# Declara un objeto de API del dashboard de Meraki en la variable dashboard
dashboard = meraki.DashboardAPI(api_key=apikey, base_url=baseurl)

# Obtén todas las organizaciones a las que tiene acceso esta llave de API
response = dashboard.organizations.getOrganizations()

# itera sobre la respuesta e imprime por fila

for row in response:
    print(row)
    print("ID de Organización: " + str(row['id']))
    print("Nombre de Organización: " + row['name'])
