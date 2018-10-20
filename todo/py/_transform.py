from dictknife import DictWalker


def withapp(d, *, prefix="app"):
    w = DictWalker(["operationId"])
    for _, sd in w.walk(d):
        if "." not in sd["operationId"]:
            sd["operationId"] = f'{prefix}.{sd["operationId"]}'
    return d
