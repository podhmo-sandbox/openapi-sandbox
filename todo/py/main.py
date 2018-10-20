import os.path
import connexion


def run(*, port: int, swagger: str) -> None:
    app = connexion.FlaskApp(__name__, specification_dir=os.path.dirname(swagger))
    app.add_api(os.path.basename(swagger))
    return app.run(port=port)


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=None)
    parser.print_usage = parser.print_help
    parser.add_argument('--port', required=True, type=int)
    parser.add_argument('--swagger', required=True)
    args = parser.parse_args(argv)
    run(**vars(args))


if __name__ == '__main__':
    main()
