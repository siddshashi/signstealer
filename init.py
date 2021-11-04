def init(file, model_dir, res):
    import sys
    sys.path.append("..")
    
    import SDEC

    x = []
    y = []

    # Load the data & split it by line breaks
    with open(file, 'r', encoding='utf-8') as t:
        new = t.read().split('\n')

    # Split the data again but this time by a tab. This will make 0 the sequence & 1 the label
    for i in range(len(new)):
        grab = new[i].split('\t')
        x.append(grab[0])
        y.append(grab[1])

    _sdd = SDEC.CreateSeqDomainDictionary(x, res)

    return _sdd