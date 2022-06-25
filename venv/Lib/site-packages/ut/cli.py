import json

import click
import yaml


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))


@click.group(cls=AliasedGroup)
def cli():
    pass


@cli.command(name='yaml2json', help='YAML -> JSON.')
@click.argument('input', type=click.File('r', encoding='utf-8'), default='-')
def cli_yaml2json(input):
    try:
        doc = yaml.load(input)
    except yaml.YAMLError as e:
        print('YAML 解析错误:', e)
    else:
        doc = json.dumps(doc, indent=2)
        print(doc, end='')


@cli.command(name='json2yaml', help='JSON -> YAML.')
@click.argument('input', type=click.File('r', encoding='utf-8'), default='-')
@click.option('--flow-style', '-f', is_flag=True, default=False)
@click.option('--explicit-start', '-e', is_flag=True, default=False)
def cli_json2yaml(input, flow_style, explicit_start):
    try:
        doc = json.load(input)
    except json.JSONDecoder as e:
        print('JSON 解析错误:', e)
    else:
        doc = yaml.dump(doc,
                        default_flow_style=flow_style,
                        explicit_start=explicit_start)
        print(doc, end='')


if __name__ == '__main__':
    cli()

