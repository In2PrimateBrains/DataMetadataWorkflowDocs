# Subject-general element schema

**Description:** Subject-general element schema generated by the CEDAR Template Editor 2.6.56

## Subject Identifier

**Label:** subjectID

**Description:** Unique identifier for the subject.

**Required:** Yes

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/9cc1f5df-566e-4651-afff-08533499af22) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectID field schema",
  "description": "subjectID field schema generated by the CEDAR Template Editor 2.6.52",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": true,
    "minLength": 2
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectID",
  "schema:description": "Unique identifier for the subject.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Identifier",
  "@id": "https://repo.metadatacenter.org/template-fields/4afe906d-683b-4a41-814d-12d144158865",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Species

**Label:** subjectSpecies

**Description:** Binomial species name from NCBI taxonomy

**Required:** Yes

**Input Type:** textfield

**Ontology Constraints:**
- National Center for Biotechnology Information (NCBI) Organismal Classification (NCBITAXON) [View Ontology](https://data.bioontology.org/ontologies/NCBITAXON)

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/76ed87e3-8c26-48ce-9d0b-e766f5513581) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectSpecies field schema",
  "description": "subjectSpecies field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield",
    "valueRecommendationEnabled": true
  },
  "_valueConstraints": {
    "requiredValue": true,
    "ontologies": [
      {
        "numTerms": 707351,
        "acronym": "NCBITAXON",
        "name": "National Center for Biotechnology Information (NCBI) Organismal Classification",
        "uri": "https://data.bioontology.org/ontologies/NCBITAXON"
      }
    ],
    "valueSets": [],
    "classes": [],
    "branches": [],
    "multipleChoice": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    },
    "@id": {
      "type": "string",
      "format": "uri"
    }
  },
  "schema:name": "subjectSpecies",
  "schema:description": "Binomial species name from NCBI taxonomy",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Species",
  "@id": "https://repo.metadatacenter.org/template-fields/ebbc2c17-b9de-41db-a70f-082c43c5d2b3",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Species Strain

**Label:** subejctSpeciesStrain

**Description:** String value indicating the strain of the species, for example: C57BL/6J.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/7cf8f57f-08f3-4025-a7bf-4b020960e00f) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subejctSpeciesStrain field schema",
  "description": "subejctSpeciesStrain field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subejctSpeciesStrain",
  "schema:description": "String value indicating the strain of the species, for example: C57BL/6J.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Species Strain",
  "@id": "https://repo.metadatacenter.org/template-fields/ef6a299f-d9d4-4fb5-ac1e-b5f98a027624",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Species Strain RRID

**Label:** subjectSpeciesStrainRRID

**Description:** Research resource identifier (RRID) of the strain of the species.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/6f1e7f82-0e0c-401e-804b-e5f7bd145525) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectSpeciesStrainRRID field schema",
  "description": "subjectSpeciesStrainRRID field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectSpeciesStrainRRID",
  "schema:description": "Research resource identifier (RRID) of the strain of the species.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Species Strain RRID",
  "@id": "https://repo.metadatacenter.org/template-fields/f5c4ec0c-b651-4f90-894e-37bf297fb956",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Trivial Name

**Label:** subjectTrivialName

**Description:** Commonly used species name.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/7afb7a78-722c-4936-9191-ec18f6a4192d) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectTrivialName field schema",
  "description": "subjectTrivialName field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield",
    "valueRecommendationEnabled": true
  },
  "_valueConstraints": {
    "requiredValue": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectTrivialName",
  "schema:description": "Commonly used species name.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Trivial Name",
  "@id": "https://repo.metadatacenter.org/template-fields/9bfa145c-744f-4887-a268-26e506c74c40",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Abbreviated Identifier

**Label:** subjectAbbreviatedID

**Description:** Abbreviated identifier of the subject, for instance, identifier used in file names.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/9d7a275f-bbdc-4094-a558-69e7e123c31a) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectAbbreviatedID field schema",
  "description": "subjectAbbreviatedID field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectAbbreviatedID",
  "schema:description": "Abbreviated identifier of the subject, for instance, identifier used in file names.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Abbreviated Identifier",
  "@id": "https://repo.metadatacenter.org/template-fields/6829fad6-08db-44e9-bfd0-8b91868229a9",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Genotypic Sex

**Label:** genotypic sex

**Description:** Sex of the subject being defined.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](http://purl.obolibrary.org/obo/PATO_0020000) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "genotypic sex field schema",
  "description": "genotypic sex field schema generated by the CEDAR Template Editor 2.6.52",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "ontologies": [],
    "valueSets": [],
    "classes": [],
    "branches": [
      {
        "source": "Neuroscience Information Framework (NIF) Standard Ontology (NIFSTD)",
        "acronym": "NIFSTD",
        "uri": "http://purl.obolibrary.org/obo/PATO_0020000",
        "name": "genotypic sex",
        "maxDepth": 0
      }
    ],
    "multipleChoice": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    },
    "@id": {
      "type": "string",
      "format": "uri"
    }
  },
  "schema:name": "genotypic sex",
  "schema:description": "Sex of the subject being defined.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Genotypic Sex",
  "@id": "https://repo.metadatacenter.org/template-fields/4da9765f-cb2d-41a3-ab14-ae9edaddf4e7",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Birthdate

**Label:** subjectBirthDate

**Description:** Birthdate of the subject, if available.

**Required:** No

**Input Type:** temporal

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/722b5953-ee99-455b-a534-2c38f73ce8cb) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectBirthDate field schema",
  "description": "subjectBirthDate field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "temporal",
    "temporalGranularity": "day"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "temporalType": "xsd:date"
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectBirthDate",
  "schema:description": "Birthdate of the subject, if available.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Birthdate",
  "@id": "https://repo.metadatacenter.org/template-fields/0ad143d7-3401-441e-a197-b047c9f9a1be",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Age

**Label:** subjectAge

**Description:** Age of the participant at time of begining of recording (first data point recorded) in years.

**Required:** Yes

**Input Type:** numeric

**Unit of Measure:** years

**Value Relation Links:** [Link](http://xmlns.com/foaf/0.1/age) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectAge field schema",
  "description": "subjectAge field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "numeric"
  },
  "_valueConstraints": {
    "requiredValue": true,
    "numberType": "xsd:decimal",
    "unitOfMeasure": "years"
  },
  "properties": {
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    },
    "@type": {
      "type": "string",
      "format": "uri"
    }
  },
  "required": [
    "@value",
    "@type"
  ],
  "schema:name": "subjectAge",
  "schema:description": "Age of the participant at time of begining of recording (first data point recorded) in years.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Age",
  "@id": "https://repo.metadatacenter.org/template-fields/22e6fcc7-b6d2-437c-9eb2-f37270832c90",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Subject Character

**Label:** subjectCharacter

**Description:** Remarks on the general characteristics of the subject, if any.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/bb8c44d6-0035-4f5d-9f3c-4f2b70ba4acc) <details>
<summary>Field Schema JSON</summary>

```json
{
  "@type": "https://schema.metadatacenter.org/core/TemplateField",
  "@context": {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "pav": "http://purl.org/pav/",
    "bibo": "http://purl.org/ontology/bibo/",
    "oslc": "http://open-services.net/ns/core#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema:name": {
      "@type": "xsd:string"
    },
    "schema:description": {
      "@type": "xsd:string"
    },
    "skos:prefLabel": {
      "@type": "xsd:string"
    },
    "skos:altLabel": {
      "@type": "xsd:string"
    },
    "pav:createdOn": {
      "@type": "xsd:dateTime"
    },
    "pav:createdBy": {
      "@type": "@id"
    },
    "pav:lastUpdatedOn": {
      "@type": "xsd:dateTime"
    },
    "oslc:modifiedBy": {
      "@type": "@id"
    }
  },
  "type": "object",
  "title": "subjectCharacter field schema",
  "description": "subjectCharacter field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield",
    "valueRecommendationEnabled": true
  },
  "_valueConstraints": {
    "requiredValue": false
  },
  "properties": {
    "@type": {
      "oneOf": [
        {
          "type": "string",
          "format": "uri"
        },
        {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "format": "uri"
          },
          "uniqueItems": true
        }
      ]
    },
    "@value": {
      "type": [
        "string",
        "null"
      ]
    },
    "rdfs:label": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "@value"
  ],
  "schema:name": "subjectCharacter",
  "schema:description": "Remarks on the general characteristics of the subject, if any.",
  "pav:createdOn": "2024-05-15T02:18:20-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:18:20-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Subject Character",
  "@id": "https://repo.metadatacenter.org/template-fields/dcbcee86-e04e-4861-975e-c244a9183004",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>
