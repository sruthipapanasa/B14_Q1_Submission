from json import load

filenames = ["demo.ipynb",
            "exploratory_visualizations.ipynb",
            "agent_responses.ipynb", 
            "agent_response_visualizations.ipynb", 
            "final_bias_visualizations.ipynb"]
for filename in filenames:
    with open(filename) as fp:
        nb = load(fp)

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(line for line in cell['source'] if not line.startswith('%'))
            exec(source, globals(), locals())