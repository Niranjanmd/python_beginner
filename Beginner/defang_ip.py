def defang(ip: str):
    splits = ip.split('.')
    seperator = '[.]'
    res = seperator.join(splits)
    return res


if __name__ == '__main__':
    print(defang('1.6'))
