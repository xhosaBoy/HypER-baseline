import os

class Data:

    def __init__(self, data_dir="data/FB15k-237", reverse=False):
        self.train_data = self.load_data(data_dir, "train", reverse=reverse)
        self.valid_data = self.load_data(data_dir, "valid", reverse=reverse)
        self.test_data = self.load_data(data_dir, "test", reverse=reverse)
        self.data = self.train_data + self.valid_data + self.test_data
        self.entities = self.get_entities(self.data)
        self.train_relations = self.get_relations(self.train_data)
        self.valid_relations = self.get_relations(self.valid_data)
        self.test_relations = self.get_relations(self.test_data)
        self.relations = self.train_relations \
                         + [i for i in self.valid_relations if i not in self.train_relations] \
                         + [i for i in self.test_relations if i not in self.train_relations]

    @staticmethod
    def load_data(dirname, data_type="train", reverse=False):
        filename = f'{data_type}.txt'
        path = os.path.join(dirname, filename)

        with open(path, 'r') as f:
            data = f.read().strip().split('\n')
            data = [i.split() for i in data]

            if reverse:
                data += [[i[2], f'{i[1]}_reverse', i[0]] for i in data]

        return data

    @staticmethod
    def get_relations(data):
        relations = sorted(list(set([d[1] for d in data])))
        return relations

    @staticmethod
    def get_entities(data):
        entities = sorted(list(set([d[0] for d in data] + [d[2] for d in data])))
        return entities
