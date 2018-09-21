def mergeDico(dico1, dico2):
    """try to merge two dictionnaries 
    test if common fields have same values (recursively as values themselves can be dictionnaires)
    if no conflict, return merged dictionary
    if conflict, return None """
    for key,val in dico1.items():
        if key in dico2.keys():
            if type(val) != dict:
                if val != dico2[key]: print(key, val, dico2 [key]);return None
            else:
                mgdsubDic = mergeDico(val, dico2[key])
                if mgdsubDic != None:
                    dico1[key] = mgdsubDic
                    dico2[key] = mgdsubDic
                else:return None
    return {**dico1, **dico2}
