#! /usr/bin/env python
# _*_ coding:UTF-8 _*_


class AttrDisplay:
    def getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s : %s]' % (self.__class__.__name__, self.getherAttrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
            # self.attr_test = self.count
            # self.attr_test = self.count + 1
            # self.count += 2


    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    x = TopTest()

    print(X)
    print(Y)
    print(x)
