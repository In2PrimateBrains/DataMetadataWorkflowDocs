import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv('.env')


def generate_markdown_summary(schema):
    md_content = f"# {schema.get('title', 'Schema Title')}\n\n"
    md_content += f"**Description:** {schema.get('description', 'No description available.')}\n\n"
    
    for prop in schema['_ui']['order']:
        prop_details = schema['properties'].get(prop, {})
        prop_ui = schema['_ui']
        is_required = prop_details.get('_valueConstraints', {}).get('requiredValue', False)
        prop_label = prop_ui['propertyLabels'].get(prop, prop)
        prop_desc = prop_ui['propertyDescriptions'].get(prop, "No description available.")
        # input_type = prop_details.get('_ui', {}).get("inputType", "Not specified")
        input_type = prop_details.get('_ui', {}).get("inputType", "Not specified")
        skos_prefLabel = prop_details.get('items', prop_details).get('skos:prefLabel', "Not specified")
        value_relation = schema['properties']['@context']['properties'].get(prop, {}).get('enum', {})
        
        md_content += f"## {skos_prefLabel}\n\n"
        md_content += f"**Label:** {prop_label}\n\n"
        md_content += f"**Description:** {prop_desc}\n\n"
        md_content += f"**Required:** {'Yes' if is_required else 'No'}\n\n"
        md_content += f"**Input Type:** {input_type}\n\n"
        
        # Summarize ontology constraints if present
        value_constraints = prop_details.get('_valueConstraints', {})
        ontologies = value_constraints.get('ontologies', [])
        if ontologies:
            md_content += "**Ontology Constraints:**\n"
            for ontology in ontologies:
                md_content += f"- {ontology['name']} ({ontology['acronym']}) [View Ontology]({ontology['uri']})\n"
            md_content += "\n"
        
        # Include "unitOfMeasure" if present
        unit_of_measure = value_constraints.get('unitOfMeasure')
        if unit_of_measure:
            md_content += f"**Unit of Measure:** {unit_of_measure}\n\n"
        
        # Include value relation links if present
        if len(value_relation) > 0:
            md_content += "**Value Relation Links:**"
            for link in value_relation:
                md_content += f" [Link]({link}) "
        
        # Collapsible section for Field Schema JSON
        md_content += "<details>\n<summary>Field Schema JSON</summary>\n\n"
        md_content += "```json\n" + json.dumps(prop_details, indent=2) + "\n```\n</details>\n\n"

    return md_content


def process_schema_folder(input_folder, output_folder=None):
    # Create the output folder based on the input folder name
    if output_folder is None:
        output_folder = f"{input_folder}-docs"
    Path(output_folder).mkdir(exist_ok=True)
    
    # List all JSON files in the specified input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            # Construct the full path for both input and output files
            input_path = os.path.join(input_folder, file_name)
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            output_path = os.path.join(output_folder, output_file_name)
            
            # Load the JSON schema
            with open(input_path, 'r') as file:
                schema = json.load(file)
            
            # Generate the Markdown summary
            markdown_summary = generate_markdown_summary(schema)
            
            # Save the Markdown summary to the output folder
            with open(output_path, 'w') as md_file:
                md_file.write(markdown_summary)
            
            print(f"Processed {file_name} -> {output_file_name}")

if __name__ == "__main__":
        
    input_folder_path = os.getenv("INPUT_FOLDER_PATH")
    output_folder_path = os.getenv("OUTPUT_FOLDER_PATH")

    process_schema_folder(input_folder_path, output_folder_path)

