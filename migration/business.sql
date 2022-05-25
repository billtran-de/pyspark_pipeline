CREATE TABLE business (
	business_id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	stars NUMERIC,
	review_count INT,
	is_open INT,
	categories VARCHAR(255),
	hours VARCHAR(255),
	checkin_count INT
)