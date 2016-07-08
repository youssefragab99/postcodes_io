from postcodes_io.helper import http_get, http_post


class Postcodes:
    def __init__(self, api_base='https://api.postcodes.io'):
        self.end_point = '{}/{}'.format(api_base, 'postcodes')

    def get(self, postcode):
        return http_get('{}/{}'.format(self.end_point, postcode))

    def get_many(self, postcodes):
        return http_post(self.end_point, data={'postcodes': postcodes})

    def nearest(self, latitude, longitude):
        return http_get(self.end_point, params={'latitude': latitude, 'longitude': longitude})

    def validate(self, postcode):
        return http_get('{}/{}/validate'.format(self.end_point, postcode))

    def nearest(self, postcode):
        return http_get('{}/{}/nearest'.format(self.end_point, postcode))

    def autocomplete(self, partial_postcode):
        return http_get('{}/{}/autocomplete'.format(self.end_point, partial_postcode))

    def query(self, postcode):
        return http_get(self.end_point, params={'q': postcode})
