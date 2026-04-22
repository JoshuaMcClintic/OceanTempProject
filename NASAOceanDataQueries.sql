-- Queries used for this project


-- Basic query to verify dataset import
SELECT *
FROM NasaData..FullDataset;

-- Easy check for NULL values
SELECT *
FROM NasaData..FullDataset
WHERE temperatureC is NULL or latitude is NULL or longitude is NULL or month is NULL or year is NULL;

-- Quick check for outliers
SELECT TOP 5 *
FROM NasaData..FullDataset
ORDER BY temperatureC DESC;
SELECT TOP 5 *
FROM NasaData..FullDataset
ORDER BY temperatureC ASC;

-- Quick check for duplicates
SELECT DISTINCT COUNT(*)
FROM NasaData..FullDataset;
SELECT COUNT(*)
FROM NasaData..FullDataset;

-- Average temp per month, year
SELECT AVG(temperatureC) as temp, month, year
FROM NasaData..FullDataset
GROUP BY month, year
ORDER BY temp;

-- Allowed me to realize that the month column was of type NVARCHAR(50)
SELECT DISTINCT month
FROM NasaData..FullDataset
ORDER BY month;