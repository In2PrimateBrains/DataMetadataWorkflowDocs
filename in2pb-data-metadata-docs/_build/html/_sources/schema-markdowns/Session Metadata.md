# Session metadata element schema

**Description:** Session metadata element schema generated by the CEDAR Template Editor 2.6.54

## Session Identifier

**Label:** sessionID

**Description:** A session is defined as the continuous time block between when the first data point is recorded after the subject is brought in and when the subject leaves. The sessionID is a unique identifier which should match the “ses-<label>” used in file naming system.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](http://www.geneontology.org/formats/oboInOwl#id) <details>
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
  "title": "sessionID field schema",
  "description": "sessionID field schema generated by the CEDAR Template Editor 2.6.54",
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
  "schema:name": "sessionID",
  "schema:description": "A session is defined as the continuous time block between when the first data point is recorded after the subject is brought in and when the subject leaves. The sessionID is a unique identifier which should match the \u201cses-<label>\u201d used in file naming system.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Session Identifier",
  "@id": "https://repo.metadatacenter.org/template-fields/c31d6e20-a6d2-481e-ab4a-a21bb7f5838a",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Session Start Date Time

**Label:** sessionStartDateTime

**Description:** Date and time of start of session. This should correspond to the first date time when the first data point of the session was recorded.

**Required:** No

**Input Type:** temporal

**Value Relation Links:** [Link](http://www.w3.org/ns/prov#startedAtTime) <details>
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
  "title": "sessionStartDateTime field schema",
  "description": "sessionStartDateTime field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "temporal",
    "temporalGranularity": "second",
    "timezoneEnabled": true,
    "inputTimeFormat": "12h"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "temporalType": "xsd:dateTime"
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
  "schema:name": "sessionStartDateTime",
  "schema:description": "Date and time of start of session. This should correspond to the first date time when the first data point of the session was recorded.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Session Start Date Time",
  "@id": "https://repo.metadatacenter.org/template-fields/2e5da7ee-6322-4571-a1e2-19af84ed57fc",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Session Duration

**Label:** sessionDuration

**Description:** The total duration of the session.

**Required:** No

**Input Type:** numeric

**Unit of Measure:** seconds

**Value Relation Links:** [Link](http://purl.obolibrary.org/obo/IAO_0000413) <details>
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
  "title": "sessionDuration field schema",
  "description": "sessionDuration field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "numeric"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "numberType": "xsd:decimal",
    "unitOfMeasure": "seconds"
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
  "schema:name": "sessionDuration",
  "schema:description": "The total duration of the session.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Session Duration",
  "@id": "https://repo.metadatacenter.org/template-fields/1b72b27e-137d-4d29-937b-888ad9f59867",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Session Quality

**Label:** sessionQuality

**Description:** A general rating of the quality of the session to simplify data screenings for further analyses.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](http://purl.obolibrary.org/obo/RO_0000086) <details>
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
  "title": "sessionQuality field schema",
  "description": "sessionQuality field schema generated by the CEDAR Template Editor 2.6.54",
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
        "source": "Semanticscience Integrated Ontology (SIO)",
        "acronym": "SIO",
        "uri": "http://semanticscience.org/resource/SIO_001293",
        "name": "quality descriptor",
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
  "schema:name": "sessionQuality",
  "schema:description": "A general rating of the quality of the session to simplify data screenings for further analyses.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Session Quality",
  "@id": "https://repo.metadatacenter.org/template-fields/0d2928be-c5de-4ab6-943d-5020a732430c",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Data Quality

**Label:** sessionDataQuality

**Description:** A general rating of the quality of the primary data signals.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](http://purl.obolibrary.org/obo/so#has_quality) <details>
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
  "title": "sessionDataQuality field schema",
  "description": "sessionDataQuality field schema generated by the CEDAR Template Editor 2.6.54",
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
        "source": "Semanticscience Integrated Ontology (SIO)",
        "acronym": "SIO",
        "uri": "http://semanticscience.org/resource/SIO_001293",
        "name": "quality descriptor",
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
  "schema:name": "sessionDataQuality",
  "schema:description": "A general rating of the quality of the primary data signals.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Data Quality",
  "@id": "https://repo.metadatacenter.org/template-fields/4383057b-f877-4ad7-947f-61c7340ce70f",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Session Comment

**Label:** comment

**Description:** General comments on the session.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](http://www.w3.org/2000/01/rdf-schema#comment) <details>
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
  "title": "comment field schema",
  "description": "comment field schema generated by the CEDAR Template Editor 2.6.54",
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
  "schema:name": "comment",
  "schema:description": "General comments on the session.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Session Comment",
  "@id": "https://repo.metadatacenter.org/template-fields/5a8de46b-38e7-447f-949f-325bc2bfe31c",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Trial Count

**Label:** trialCount

**Description:** Total number of trials within a session.

**Required:** No

**Input Type:** numeric

**Value Relation Links:** [Link](http://www.geneontology.org/formats/oboInOwl#count) <details>
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
  "title": "trialCount field schema",
  "description": "trialCount field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "numeric"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "numberType": "xsd:decimal"
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
  "schema:name": "trialCount",
  "schema:description": "Total number of trials within a session.",
  "pav:createdOn": "2024-03-25T08:05:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-03-25T08:05:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Trial Count",
  "@id": "https://repo.metadatacenter.org/template-fields/160a2326-a250-4505-a525-3be8355e6bbe",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>
