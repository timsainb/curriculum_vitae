import jinja2
import json
import re
import datetime
from pathlib2 import Path

now = datetime.datetime.now()

PROJECT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = PROJECT_DIR / "templates"
DATA_PATH = PROJECT_DIR / "data"
BUILD_PATH = PROJECT_DIR / "cv"
MYNAME = "Tim Sainburg"


def load_data(json_glob):
    def _ordinal_day(e):
        return -datetime.date(
            e.get("year", 1), e.get("month", 1), e.get("day", 1)
        ).toordinal()

    datas = []
    for json_file in json_glob:
        with open(json_file) as f:
            try:
                data = json.load(f)
            except:
                raise Exception('JSON wont load: {}'.format(json_file)) 
            data = {k: sorted(v, key=_ordinal_day) for k, v in data.items()}
            entries = list(data.values())[0]
            for entry in entries:
                # if the datetime is in the future, replace with (to appear)
                if "day" in entry and "month" in entry and "year" in entry:
                    entry_time = datetime.datetime(
                        entry["year"], entry["month"], entry["day"]
                    )
                    if entry_time > now:
                        entry["year"] = "{} (to appear)".format(entry["year"])
                # bold my name
                if "authors" in entry:
                    entry["authors"] = re.sub(
                        r"({})".format(MYNAME), r"<b>\1</b>", entry["authors"]
                    )
            datas.append(data)

    return dict((k, v) for d in datas for (k, v) in d.items())


def compile_template(template_path, data, output_path):
    env = jinja2.environment.Environment(
        loader=jinja2.FileSystemLoader(template_path.parent.as_posix())
    )
    template = env.get_template(template_path.name)
    with open(output_path, "w") as f:
        f.write(template.render(**data))


if __name__ == "__main__":
    # for each template, compile the template
    for template_file in list(TEMPLATE_PATH.glob("*.tpl")):
        compile_template(
            template_file,
            load_data(list(DATA_PATH.glob("*.json"))),
            BUILD_PATH / "{}.html".format(template_file.stem),
        )
