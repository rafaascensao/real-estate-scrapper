class Idealista():
    def __init__(self, parameters: dict, filters: dict = {}, tipology: list = []):
        self.url = f"https://www.idealista.pt/{parameters['buy_or_rent']}-{parameters['type']}/{parameters['location']}/"
        if filters.keys() or tipology:
            preference_list = [pref + '_' + str(value) for pref, value in filters.items()]
            preference_list.extend(tipology)
            self.url = self.url + 'com-' + ','.join(preference_list)


if __name__ == '__main__':
    parameters = {'buy_or_rent': 'arrendar', 'type': 'casas', 'location': 'lisboa'}
    prefs = {'preco-max': 1500, 'preco-min': 100, 'tamanho-min': 40}
    i = Idealista(parameters, filters=prefs, tipology=['t2'])
    print(i.url)