import sys
import requests
import json 

def is_flag(arg: str) -> bool:
    """Check if the arg is a flag"""
    return arg.startswith('-')


def arg_to_flag(arg: str) -> str:
    """
    Given the argument convert it to flag
    remove - and --
    """
    # TODO should check for validity of the flag
    assert arg.startswith('-'), "Invalid argument for flag, doesnt star with -"

    arg = arg.removeprefix('-')
    arg = arg.removeprefix('-')
    match arg: 
        case 'X' | 'request':  
            return 'method'
        case _ :
            assert 1==1, "NOT IMPLEMENTED"
            return ''


def create_arg_dict(args: list[str]) -> dict:
    """Parse the arguments, return a structured dict"""
    arg_dict = {}

    i = 0
    while i < len(args):
        arg = args[i]
        if is_flag(arg):
            flag = arg_to_flag(arg)
            i+=1
            val = args[i]
            # TODO: carefully remove quotes
            val.replace("'", '')
            arg_dict[flag] = val
        else:
            # assuming this is the url 
            # TODO: maybe add some check
            arg_dict['url'] = arg
        i+=1

    return arg_dict


def print_res(res: requests.Response):
    status_code = res.status_code
    print(f'status code : {status_code}')

    if res.status_code != 200:
        # TODO: Explain the status code to me
        print(f'status code: {status_code}')
        print(f'means: boohoo')
    else:
        # TODO: assuming that the res has a json 
        res_json = res.json()
        print(f'out ----------------')
        print(json.dumps(res_json, indent=4))


def make_req(arg_dict) -> None:
    method = arg_dict.get('method', 'GET')
    url = arg_dict.get('url')

    if url is None:
        print("[ERR] No URL provided")
        exit(1)
    
    # TODO: requests doesnt needs complete url with http or https
    match method:
        case 'GET':
            res = requests.get(url)
        case 'POST':
            res = requests.post(url)
        case _: 
            res = None
            print('[ERR] method not implemented')

    if res:
        print_res(res)

def main(args: list[str]):
    arg_dict = create_arg_dict(args)
    # print(arg_dict)
    make_req(arg_dict)


if __name__ == "__main__":
    # remove the filename
    args = sys.argv[1:]
    main(args)
