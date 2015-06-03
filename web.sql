-- phpMyAdmin SQL Dump
-- version 4.0.10
-- http://www.phpmyadmin.net
--
-- Host: Irfan Hariansyah
-- Generation Time: Jun 04, 2015 at 01:32 AM
-- Server version: 5.6.19-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `web`
--
CREATE DATABASE IF NOT EXISTS `web` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `web`;

--
-- Table structure for table `berita`
--

CREATE TABLE IF NOT EXISTS `berita` (
  `news_id` int(8) NOT NULL AUTO_INCREMENT,
  `news_title` varchar(64) NOT NULL,
  `news_date` varchar(64) DEFAULT NULL,
  `news_content` text,
  `news_img` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=40 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
