swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Health Calculator API",
        "description": "API for calculating BMI and BMR",
        "version": "1.0.0"
    },
    "host": "127.0.0.1:5000",
    "basePath": "/",
    "schemes": ["http"],
    "paths": {
        "/bmi": {
            "post": {
                "summary": "Calculate BMI",
                "description": "Compute BMI based on height and weight",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "height": {"type": "number", "example": 1.75},
                                "weight": {"type": "number", "example": 70}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "BMI calculation result",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "operation": {"type": "string", "example": "BMI Calculation"},
                                "bmi": {"type": "number", "example": 22.86}
                            }
                        }
                    },
                    "400": {"description": "Missing parameters"}
                }
            }
        },
        "/bmr": {
            "post": {
                "summary": "Calculate BMR",
                "description": "Compute BMR based on height, weight, age, and gender",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "height": {"type": "number", "example": 175},
                                "weight": {"type": "number", "example": 70},
                                "age": {"type": "integer", "example": 25},
                                "gender": {"type": "string", "enum": ["male", "female"], "example": "male"}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "BMR calculation result",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "operation": {"type": "string", "example": "BMR Calculation"},
                                "bmr": {"type": "number", "example": 1766.85}
                            }
                        }
                    },
                    "400": {"description": "Missing parameters"}
                }
            }
        }
    }
}
