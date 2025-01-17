#[allow(dead_code)]
mod ascii;
mod git;
mod reinstall;
mod test;

use std::path::PathBuf;

use ascii::{CYAN, YELLOW};
use clap::{arg, Command};

fn cli() -> Command {
    Command::new("eve")
    .about("A CLI Made for Eveeifyeve")
    .version("1.0.2")
    .subcommand_required(true)
    .arg_required_else_help(true)
    .allow_external_subcommands(true)
    .subcommand(
        Command::new("statusr")
        .about("Checks if you have commited in folders")
        .arg(arg!(<PATH> "").value_parser(clap::value_parser!(PathBuf)))
    )
    .subcommand(
        Command::new("gitr")
            .about("Checks if you have commited in multiple folders")
            .arg(arg!(<ARGS>... "").value_parser(clap::value_parser!(String)))
    )
    .subcommand(Command::new("reinstall").about("Reinstalls Eveeifyeve"))
    .help_template(format!("{}{{name}} {{version}}\n{{author-with-newline}}{{about-with-newline}}\n{{usage-heading}} {{usage}}\n\n {}Commands: \n{{subcommands}}\n {}Options: \n{{options}}", CYAN, YELLOW, YELLOW))
}

fn main() {
    let commands = cli().get_matches();

    match commands.subcommand() {
        Some(("statusr", sub_match)) => {
            if let Some(path) = sub_match.get_one::<PathBuf>("PATH") {
                git::statusr(path)
            }
        }
        Some(("reinstall", _)) => {
            reinstall::main();
        }

        _ => unreachable!(),
    }
}
