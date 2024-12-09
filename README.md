# API Documentation

## Base URL
`https://api.assisterr.ai/`

---

## Endpoints

### 1. [POST] /api/v1/slm/{handel_name}/chat/
**Description:** Request to receive a response from SLM without context binding (without keeping history).

**Headers:**
| Header       | Required | Example Value                                         | Description                |
|--------------|----------|-------------------------------------------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`                                          | API Key for authentication.|

**Path Parameters:**
| Parameter      | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `handel_name`  | string | Yes      | Unique identifier for the slm.    |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```

### 1. [POST] /api/v1/slm/{handel_name}/chat/stream/
**Description:** Request to receive a stream (SSE) response from SLM without context binding (without keeping history).

**Headers:**
| Header       | Required | Example Value        | Description                |
|--------------|----------|----------------------|----------------------------|
| `X-Api-Key`  | Yes      | `your_token`         | API Key for authentication.|

**Path Parameters:**
| Parameter      | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `handel_name`  | string | Yes      | Unique identifier for the slm.    |

**Request Body (JSON):**
```json
{
  "query": "Your query here"
}
```
