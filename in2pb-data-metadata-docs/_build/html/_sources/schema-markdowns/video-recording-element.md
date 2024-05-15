# Video recording metadata element schema

**Description:** Video recording metadata element schema generated by the CEDAR Template Editor 2.6.56

## Video Identifier

**Label:** videoID

**Description:** Identifier for the video recording.

**Required:** Yes

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/2351b0b4-0d23-4e4f-93e9-a41d836af861) <details>
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
  "title": "videoID field schema",
  "description": "videoID field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": true
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
  "schema:name": "videoID",
  "schema:description": "Identifier for the video recording.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Identifier",
  "@id": "https://repo.metadatacenter.org/template-fields/b7fa5a3c-3022-4acc-89ed-4a3273398202",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video File Format

**Label:** videoFileFormat

**Description:** The format of the video file, such as, "MP4", "AVI", "MOV", etc.

**Required:** Yes

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/2d5ddfac-c3d1-4cb5-a550-c96a394365a3) <details>
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
  "title": "videoFileFormat field schema",
  "description": "videoFileFormat field schema generated by the CEDAR Template Editor 2.6.56",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": true
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
  "schema:name": "videoFileFormat",
  "schema:description": "The format of the video file, such as, \"MP4\", \"AVI\", \"MOV\", etc.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video File Format",
  "@id": "https://repo.metadatacenter.org/template-fields/65a9d873-7aef-4e0d-9a96-541f0f327174",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video Codec

**Label:** videoCodec

**Description:** If the video is compressed, what codec was used. Enter none if not applicable.

**Required:** Yes

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/39059fb2-968d-47f8-ba64-b7bc2bfdb2e4) <details>
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
  "title": "videoCodec field schema",
  "description": "videoCodec field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "textfield"
  },
  "_valueConstraints": {
    "requiredValue": true
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
  "schema:name": "videoCodec",
  "schema:description": "If the video is compressed, what codec was used. Enter none if not applicable.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Codec",
  "@id": "https://repo.metadatacenter.org/template-fields/c2a17347-bd45-48ad-8236-f909cf46b4db",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video Source

**Label:** videoSource

**Description:** The source of the video file, for instance, "Camera [name]", "Screen capture", etc.

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/474a7fb5-e5ad-459a-ae9b-9a6262819a1c) <details>
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
  "title": "videoSource field schema",
  "description": "videoSource field schema generated by the CEDAR Template Editor 2.6.54",
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
  "schema:name": "videoSource",
  "schema:description": "The source of the video file, for instance, \"Camera [name]\", \"Screen capture\", etc.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Source",
  "@id": "https://repo.metadatacenter.org/template-fields/b2662123-fc55-4a60-95c7-29dacf8b8d80",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video Resolution Width

**Label:** videoResolutionWidth

**Description:** The resolution width of the video file in pixels.

**Required:** No

**Input Type:** numeric

**Unit of Measure:** px

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/85005e56-86cd-4305-be6b-91e8d533cc8f) <details>
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
  "title": "videoResolutionWidth field schema",
  "description": "videoResolutionWidth field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "numeric"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "numberType": "xsd:decimal",
    "unitOfMeasure": "px"
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
  "schema:name": "videoResolutionWidth",
  "schema:description": "The resolution width of the video file in pixels.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Resolution Width",
  "@id": "https://repo.metadatacenter.org/template-fields/a7bdfc03-7158-450b-89c0-10e5c31e3d1b",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video Resolution Height

**Label:** videoResolutionHeight

**Description:** The resolution height of the video file in pixels.

**Required:** No

**Input Type:** numeric

**Unit of Measure:** px

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/9f3cd350-ab28-4f6e-99cf-39247bc2d9db) <details>
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
  "title": "videoResolutionHeight field schema",
  "description": "videoResolutionHeight field schema generated by the CEDAR Template Editor 2.6.54",
  "_ui": {
    "inputType": "numeric"
  },
  "_valueConstraints": {
    "requiredValue": false,
    "numberType": "xsd:decimal",
    "unitOfMeasure": "px"
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
  "schema:name": "videoResolutionHeight",
  "schema:description": "The resolution height of the video file in pixels.",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Resolution Height",
  "@id": "https://repo.metadatacenter.org/template-fields/9dd17df3-4726-44f4-bed8-1b9db8077756",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>

## Video Aspect Ratio

**Label:** videoAspectRatio

**Description:** The aspect ratio of the video file, in the format, width:height

**Required:** No

**Input Type:** textfield

**Value Relation Links:** [Link](https://schema.metadatacenter.org/properties/39401c3b-c90f-4916-83d9-f6c53e7c3415) <details>
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
  "title": "videoAspectRatio field schema",
  "description": "videoAspectRatio field schema generated by the CEDAR Template Editor 2.6.54",
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
  "schema:name": "videoAspectRatio",
  "schema:description": "The aspect ratio of the video file, in the format, width:height",
  "pav:createdOn": "2024-05-15T02:21:53-07:00",
  "pav:createdBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "pav:lastUpdatedOn": "2024-05-15T02:21:53-07:00",
  "oslc:modifiedBy": "https://metadatacenter.org/users/f3d8067f-c204-45c0-8fb1-8393e486593c",
  "schema:schemaVersion": "1.6.0",
  "additionalProperties": false,
  "skos:prefLabel": "Video Aspect Ratio",
  "@id": "https://repo.metadatacenter.org/template-fields/e3318a08-43ec-42db-b815-acee1100d4f0",
  "$schema": "http://json-schema.org/draft-04/schema#"
}
```
</details>
