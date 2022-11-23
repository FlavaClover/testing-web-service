import argparse
import sys
import time
from threading import Thread

import config
import server
import client


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('Testing of synchronous web-service')

    parser.add_argument(
        '--host', '-H', help='Set server\'s host', type=str,
        default=config.HOST
    )
    parser.add_argument(
        '--port', '-p', help='Set server\'s port', type=int,
        default=config.PORT
    )

    parser.add_argument(
        '--count', '-c', help='Set client\'s count', type=int,
        default=1
    )

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    server_thread = Thread(target=server.server, args=(args.host, args.port), daemon=True)
    server_thread.start()

    client.requests(args.count, args.host, args.port)

    server_thread.join()


if __name__ == '__main__':
    main()
