import json
import time

def main():
    print("Nombre de la red ?")
    name = input()
    print("Descripcion:")
    descripcion = input()

    data = {
        "name": name,
        "descriptions": descripcion,
        "date": {"day": time.strftime("%d/%m/%y"), "hour":time.strftime("%H:%M:%S")},
        "train": {"size": 213, "error": 0.48524},
        "data_characteristics":{
                                    "layers_lengths":[4,3,1],
                                    "total_neurons": 4,
                                    "number_of_entries": 3,
                                    "number_of_departures": 1,
                                    "number_of_hidden_layers": 1,
                                    "data_type": "fload",
        },
        "layers_data":[
                        [
                            {
                                "size_tickets": 4,
                                "memory": True,
                                "references_entries":[(1,4), (1,2), (0,7), (0,8)],
                                "memory_data":[ [(1,8),2] ],
                                "w":[1,2,3,4],
                                "b":1,
                                "function": "cualquiera",
                            },
                            {
                                "size_tickets": 4,
                                "memory": True,
                                "references_entries":[(1,4), (1,2), (0,7), (0,8)],
                                "memory_data":[ [(1,8),2] ],
                                "w":[1,2,3,4],
                                "b":1,
                                "function": "cualquiera",
                            },
                            {
                                "size_tickets": 4,
                                "memory": True,
                                "references_entries":[(1,4), (1,2), (0,7), (0,8)],
                                "memory_data":[ [(1,8),2] ],
                                "w":[1,2,3,4],
                                "b":1,
                                "function": "cualquiera",
                            }
                        ],
                        [
                            {
                                "size_tickets": 4,
                                "references_entries":[(1,4), (1,2), (0,7), (0,8)],
                                "memory":False,
                                "w":[1,2,3,4],
                                "b":1,
                                "function": "cualquiera",
                            }
                        ]
                    ]
    }
    data.update({"name":"carlos", "adqawd":2})
    with open('Prueba.json', 'w') as file:
        json.dump(data, file)


    with open('Prueba.json') as file:
        data1 = json.load(file)
        print(type(data1))
        print(data1["name"])
        print(data1["layers_data"][0][0]["size_tickets"])
        print(data1["date"]["day"])
        print(data1["date"]["hour"])
        print(data1["descriptions"])

        for neuron in data1["layers_data"][0]:
            print(neuron["w"])

if __name__ == '__main__':
    main()

