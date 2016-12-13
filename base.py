from OSC import OSCClient, OSCBundle

DEFAULTPORT = 54345

class PacketManager(object):
    def __init__(self, num_datapoints, port=DEFAULTPORT):
        self.num_datapoints = num_datapoints
        self.data_sources = []

        self.client = OSCClient()
        self.client.connect(("localhost", port))

    def add_data_source(self, data_source):
        self.data_sources.append(data_source)

    def send_to_max(self):
        bundle = OSCBundle()
        x_range = range(6)
        for i, data_source in enumerate(self.data_sources):
            bundle.append({'addr': "/a/note/x",
                           'args':x_range})
            bundle.append({'addr': "/a/note/y",
                           'args':data_source.notes[0]})
            bundle.append({'addr': "/a/rest/x",
                           'args':x_range})
            bundle.append({'addr': "/a/rest/y",
                           'args':data_source.notes[1]})
            bundle.append({'addr': "/b/note/x",
                           'args':x_range})
            bundle.append({'addr': "/b/note/y",
                           'args':data_source.buffer[0]})
            bundle.append({'addr': "/b/rest/x",
                           'args':x_range})
            bundle.append({'addr': "/b/rest/y",
                           'args':data_source.buffer[1]})

        self.client.send(bundle)


class DataSource(object):
    def __init__(self, num_datapoints, filename):
        self.num_datapoints = num_datapoints
        self.filename = filename

    @property
    def data(self):
        print("calling here")
        raise NotImplementedError

    def zero_hold(self, data, hold):
        new_data = []
        len_data = len(data)
        i = 0
        while len(new_data) < len_data * hold and i < len_data:
            for _ in range(hold):
                new_data.append(data[i])
            i += 1

        i = 0
        while len(new_data) < self.num_datapoints and i < len_data:
            for _ in range(hold):
                new_data.append(data[i])
            i += 1
        return new_data


class DummyDataSource(DataSource):
    @property
    def data(self):
        return [0 for _ in xrange(self.num_datapoints)]

if __name__ == '__main__':
    pm = PacketManager(3)
    dds = DummyDataSource(3)

    pm.add_data_source(dds)
    pm.add_data_source(dds)
    pm.add_data_source(dds)

    pm.send_to_max()