from mininet.topo import Topo


class SpineLeafTopo(Topo):

    def build(self):
        spines = [self.addSwitch('s{}'.format(i)) for i in range(1, 3)]
        leaves = [self.addSwitch('s{}'.format(i)) for i in range(3, 7)]

        for idx, leaf in enumerate(leaves, start=1):
            host = self.addHost('h{}'.format(idx))
            self.addLink(leaf, host)

        for spine in spines:
            for leaf in leaves:
                self.addLink(spine, leaf)


topos = {'spineleaf': (lambda: SpineLeafTopo())}
