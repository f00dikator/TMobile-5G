import argparse
from tmobileClass import tmobile
import pdb

def main(t_session):
    """
    Main entry point
    :param t_session: tmobile session object
    :return: None
    """

    if args.show_all:
        t_session.show_all()
        exit(0)

    if args.lan_stats:
        t_session.lan_status()

    if args.wan_stats:
        t_session.wan_status()

    if args.main_config:
        t_session.main_status()

    if args.data_fields:
        t_session.data_fields()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Performs Recon on the T-Mobile Internet Gateway 4G/5G device')
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbosity', help='Verbose logging enabled')
    parser.add_argument('-i', '--ip', action='store', dest='ip_address', help='The IP address to scan')
    parser.add_argument('-l', '--lan_stats', action='store_true', dest='lan_stats', help='Show LAN stats')
    parser.add_argument('-w', '--wan_stats', action='store_true', dest='wan_stats', help='Show WAN stats')
    parser.add_argument('-c', '--config', action='store_true', dest='main_config',
                        help='Shows device configuration as well as all attached devices')
    parser.add_argument('-d', '--data_fields', action='store_true', dest='data_fields',
                        help='Show the different form fields and their expected format')
    parser.add_argument('-a', '--all', action='store_true', dest='show_all',
                        help='Grabs *all* of the config/stats (can be a lot of data)')

    parser.set_defaults(verbosity=False)

    args = parser.parse_args()

    if args.verbosity:
        level = 'DEBUG'
    else:
        level = 'INFO'

    print('Executing T-Mobile Recon')

    if not args.ip_address:
        print("You must enter -i IP_ADDRESS")
        exit(0)

    t_session = tmobile(ip=args.ip_address)

    main(t_session)


