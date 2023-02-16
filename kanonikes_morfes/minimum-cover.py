from rdt import DataDependency

fd = DataDependency(["A -> B", "B -> C", "C -> D"])

minimal_cover = fd.minimal_cover()
print(minimal_cover)
